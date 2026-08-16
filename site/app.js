(function () {
  "use strict";

  var dataset = window.AFRPOWEROS;
  var geo = window.AFRICA_GEO;

  if (!dataset || !geo) {
    document.getElementById("heroMeta").textContent = "Dataset failed to load.";
    return;
  }

  var STATUS_LABEL = {
    Operating: "Operating",
    "Under Construction": "Under Construction",
    Announced: "Announced",
    Preparing: "Preparing",
    Exploring: "Exploring",
    None: "None"
  };

  var STATUS_COLOR = {
    Operating: "#34c759",
    "Under Construction": "#ff9f0a",
    Announced: "#ffd60a",
    Preparing: "#0a84ff",
    Exploring: "#bf5af2",
    None: "#8e8e93"
  };

  var NAME_ALIAS = {
    Tanzania: "United Republic of Tanzania",
    "Congo (Dem. Rep.)": "Dem. Rep. Congo",
    "Côte d'Ivoire": "Côte d'Ivoire"
  };

  var byName = {};
  dataset.countries.forEach(function (rec) {
    byName[rec.country] = rec;
    byName[NAME_ALIAS[rec.country]] = rec;
  });

  function bbox(features) {
    var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    features.forEach(function (f) {
      eachCoord(f.geometry, function (lon, lat) {
        if (lon < minX) minX = lon;
        if (lon > maxX) maxX = lon;
        if (lat < minY) minY = lat;
        if (lat > maxY) maxY = lat;
      });
    });
    return { minX: minX, minY: minY, maxX: maxX, maxY: maxY };
  }

  function eachCoord(geom, fn) {
    if (!geom) return;
    if (geom.type === "Polygon") {
      geom.coordinates.forEach(function (ring) { ring.forEach(function (c) { fn(c[0], c[1]); }); });
    } else if (geom.type === "MultiPolygon") {
      geom.coordinates.forEach(function (poly) {
        poly.forEach(function (ring) { ring.forEach(function (c) { fn(c[0], c[1]); }); });
      });
    }
  }

  function ringPath(ring) {
    var parts = [];
    for (var i = 0; i < ring.length; i++) {
      var p = project(ring[i][0], ring[i][1]);
      var cmd = i === 0 ? "M" : "L";
      parts.push(cmd + p.x + " " + p.y);
    }
    parts.push("Z");
    return parts.join("");
  }

  function polygonPath(poly) {
    return poly.map(ringPath).join(" ");
  }

  function featurePath(geom) {
    if (!geom) return "";
    if (geom.type === "Polygon") return polygonPath(geom.coordinates);
    if (geom.type === "MultiPolygon") return geom.coordinates.map(polygonPath).join(" ");
    return "";
  }

  var SIZE = 1000;
  var PAD = 16;
  var box = bbox(geo);
  var w = box.maxX - box.minX;
  var h = box.maxY - box.minY;
  var scale = Math.min((SIZE - PAD * 2) / w, (SIZE - PAD * 2) / h);
  var offX = (SIZE - w * scale) / 2 - box.minX * scale;
  var offY = (SIZE - h * scale) / 2 + box.maxY * scale;

  function project(lon, lat) {
    return { x: round(lon * scale + offX), y: round(-lat * scale + offY) };
  }

  var svg = document.getElementById("mapSvg");
  var tooltip = document.getElementById("tooltip");

  function recFor(f) {
    return byName[f.name];
  }

  function fillFor(f) {
    var rec = recFor(f);
    if (!rec) return "#d2d2d7";
    return STATUS_COLOR[rec.program_status] || "#8e8e93";
  }

  var rows = {};

  geo.forEach(function (f) {
    var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("class", "country");
    path.setAttribute("d", featurePath(f.geometry, project));
    path.setAttribute("fill", fillFor(f));
    path.setAttribute("data-name", f.name);
    path.setAttribute("data-iso", f.iso || "");
    svg.appendChild(path);
    rows[f.name] = path;
  });

  function showTooltip(html, x, y) {
    tooltip.innerHTML = html;
    tooltip.hidden = false;
    var rect = svg.parentElement.getBoundingClientRect();
    var tx = x - rect.left + 14;
    var ty = y - rect.top - 10;
    if (tx + tooltip.offsetWidth > rect.width) tx = x - rect.left - tooltip.offsetWidth - 14;
    if (ty < 0) ty = 0;
    tooltip.style.left = tx + "px";
    tooltip.style.top = ty + "px";
  }

  function hideTooltip() {
    tooltip.hidden = true;
  }

  function tooltipHTML(f) {
    var rec = recFor(f);
    if (!rec) {
      return "<h4>" + f.name + "</h4><p>No record yet — contribute one.</p>";
    }
    var lines = [];
    lines.push("<strong>" + rec.program_status + "</strong>");
    if (rec.iaea_milestone_phase) lines.push("IAEA Phase " + rec.iaea_milestone_phase);
    if (rec.capacity_gw_planned) lines.push(rec.capacity_gw_planned + " GW planned");
    if (rec.first_grid_target_year) lines.push("Grid ~" + rec.first_grid_target_year);
    lines.push(rec.confidence + " · " + rec.last_verified);
    return "<h4>" + rec.country + "</h4><p>" + lines.join(" · ") + "</p>";
  }

  svg.addEventListener("mousemove", function (e) {
    var target = e.target;
    if (!target || target.getAttribute("class") !== "country") {
      hideTooltip();
      return;
    }
    showTooltip(tooltipHTML(target), e.clientX, e.clientY);
  });

  svg.addEventListener("mouseleave", hideTooltip);

  svg.addEventListener("click", function (e) {
    var target = e.target;
    if (!target || target.getAttribute("class") !== "country") return;
    var name = target.getAttribute("data-name");
    var tr = document.getElementById("row-" + name.replace(/\s+/g, "-"));
    if (!tr) return;
    tr.scrollIntoView({ behavior: "smooth", block: "center" });
    tr.classList.remove("highlight");
    void tr.offsetWidth;
    tr.classList.add("highlight");
  });

  var legend = document.getElementById("legend");
  Object.keys(STATUS_LABEL).forEach(function (key) {
    var item = document.createElement("span");
    item.className = "item";
    item.innerHTML =
      '<span class="swatch" style="background:' + STATUS_COLOR[key] + '"></span>' + STATUS_LABEL[key];
    legend.appendChild(item);
  });

  var noRec = document.createElement("span");
  noRec.className = "item";
  noRec.innerHTML = '<span class="swatch" style="background:#d2d2d7"></span>No record';
  legend.appendChild(noRec);

  var tableBody = document.getElementById("tableBody");
  var tpl = document.createElement("template");

  dataset.countries
    .slice()
    .sort(function (a, b) { return a.country.localeCompare(b.country); })
    .forEach(function (rec) {
      tpl.innerHTML =
        '<tr id="row-' + rec.country.replace(/\s+/g, "-") + '">' +
        "<td><strong>" + rec.country + "</strong></td>" +
        '<td><span class="tag" style="background:' + STATUS_COLOR[rec.program_status] + '">' +
        STATUS_LABEL[rec.program_status] + "</span></td>" +
        "<td>" + (rec.iaea_milestone_phase || "—") + "</td>" +
        "<td>" + (rec.capacity_gw_planned != null ? rec.capacity_gw_planned + " GW" : "—") + "</td>" +
        "<td>" + (rec.first_grid_target_year || "—") + "</td>" +
        "<td>" + rec.regulator + "</td>" +
        '<td><span class="tag tag-unverified">' + rec.confidence + "</span></td>" +
        "</tr>";
      tableBody.appendChild(tpl.content.firstChild);
    });

  document.getElementById("heroMeta").textContent =
    dataset.countries.length + " countries · " +
    dataset.generated + " · every fact sourced and confidence-labelled";
})();
