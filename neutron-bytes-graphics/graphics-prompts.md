# AfrPowerOS — High-Fidelity Graphic Generation Prompts

HOW TO USE
---------
1. Paste the shared "Design System" section plus ONE numbered graphic spec into your AI
   (image generator or code/svg generator). If the AI can produce vector/code (SVG,
   HTML/CSS, React, Python/matplotlib/Pillow), prefer that — it guarantees exact layout.
2. Do not let the AI invent or change any number. Every data value is given explicitly.
3. Spelling is exact: "AfrPowerOS", "El Dabaa", "Koeberg", "IRP 2025". Do not modify.
4. All canvases are designed at a 2000px base width. Export at 2x (4000px wide) so print
   and high-DPI web both stay sharp. Provide PNG and JPG.

================================================================================
SHARED DESIGN SYSTEM (use in all three graphics)
================================================================================

CANVAS / BACKGROUND
- Canvas base width: 2000 px. Background color: #FBF9F7 (warm off-white paper).
- No border, no frame, no watermark. No drop shadows anywhere unless stated.
- Keep 96 px of clear gutter margin on all four sides of the canvas.

COLOR PALETTE (exact hex only)
- Paper background      #FBF9F7
- Ink (primary text)    #16181D
- Secondary text        #5C6670
- Muted / tertiary      #8A94A0
- Hairline / borders    #E3E0DC
- Faint chart track     #F0ECE6
- Status – Operating           #1B4332  (deep forest green)
- Status – Under construction  #B85C1C  (burnt sienna / amber)
- Status – Preparing           #1D4ED8  (strong blue)
- Status – Exploring           #64748B  (slate blue-gray)
- Status – No program          #A3ACB8  (pale slate)
- Brand accent (kicker text)   #1D4ED8

TYPOGRAPHY (font stack: 'Inter', 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif)
- Kicker label : 16 px, weight 600, UPPERCASE, letter-spacing +3 px, color #1D4ED8
- Title (H1)   : 54 px, weight 700, letter-spacing -1 px, color #16181D
- Subtitle     : 24 px, weight 400, letter-spacing 0, color #5C6670
- Body/labels  : 19–22 px, weight 500/600, color #16181D
- Big numbers  : 48–56 px, weight 700, letter-spacing -1 px, color #16181D
- Caption/credit footer : 13 px, weight 400, color #8A94A0
- All text left-aligned unless specified. No text shadows or outlines.

GENERAL FOOTER (all three graphics, bottom-left near y = canvas_height - 48)
"Source: AfrPowerOS open dataset (data/afrpoweros.json) · Verified 2026-08-16" in
13 px #8A94A0. Second line: "Credit: AfrPowerOS — open, cited data on Africa's
civilian nuclear programs · CC BY 4.0" in 13 px #8A94A0.

STATUS COLOR KEY (semantic — never change)
- Operating           #1B4332
- Under construction  #B85C1C
- Preparing           #1D4ED8
- Exploring           #64748B
- No program          #A3ACB8

================================================================================
GRAPHIC 1 — PLANNED NUCLEAR CAPACITY BY COUNTRY (horizontal bar chart)
================================================================================

CANVAS: 2000 x 1400 px, background #FBF9F7.

HEADER BLOCK (top-left corner, all starting at x = 96)
- y=96  : kicker "AFRPOWEROS · OPEN DATA" (16px/600/+3px, #1D4ED8, uppercase)
- y=142 : H1 title "Planned Nuclear Capacity by Country" (54px/700/-1px, #16181D)
- y=196 : subtitle "Gigawatts planned · first-grid target year in parentheses,
          where announced" (24px/400, #5C6670)

LEGEND (horizontal row, y=300)
- Five chips, left to right starting at x=96, 200 px apart:
  Operating (#1B4332), Under construction (#B85C1C), Preparing (#1D4ED8),
  Exploring (#64748B), No program (#A3ACB8).
- Chip = 18x18 px square swatch with 16 px radius, then an 18 px weight-500 label in
  #16181D, 12 px space between swatch and label.

CHART AREA
- Left category-label column: text right-aligned, ending exactly at x = 470.
- Plot area: x from 520 to 1904. Scale: 1 GW = 130 px of bar length.
- Chart horizontal gridlines none (only faint vertical lines below).
- 7 horizontal bars, rows sorted LARGEST on TOP. Bar height 64 px, row pitch 117 px.
  Row center y for i=0..6: y = 540 + i*117.
- Each bar sits on a full-length faint track extending from x=520 to x=1720 in #F0ECE6,
  height 64 px, so the viewer always sees the full scale.

BARS (value, color, row):
  Row 0  Uganda             8.4 GW  #1D4ED8   (Preparing)    first-grid year 2031
  Row 1  South Africa       5.2 GW  #1B4332   (Operating)    first-grid year 2036
  Row 2  Egypt              4.8 GW  #B85C1C   (Under construction)  target 2028
  Row 3  Nigeria            4.0 GW  #1D4ED8   (Preparing)    year n/a
  Row 4  Kenya              2.0 GW  #1D4ED8   (Preparing)    first-grid year 2034
  Row 5  Ghana              1.0 GW  #1D4ED8   (Preparing)    first-grid year 2030
  Row 6  Zambia             1.0 GW  #64748B   (Exploring)    year n/a
  Zimbabwe/Eswatini etc. are Exploring but have no announced GW — do NOT draw them.
- Bar width = value GW x 130 px (so Uganda = 8.4x130 = 1092 px, drawn from x=520,
  ending x=1612). Bar has fully rounded ends (radius = 32 px = half of 64 px height).

CATEGORY LABELS (right-aligned ending at x=470, vertically centered on each bar):
  20 px weight 600 #16181D for the country name, followed by a regular 18 px weight 400
  #5C6670 " · 20XX" for the first-grid year (omit " · year" when n/a).
  Center each label on its bar's row center y.

VALUE LABELS: "X.X GW" placed 28 px to the right of each bar end, vertically centered
  on the bar, 22 px weight 600, color #16181D, no units symbol change.

X-AXIS
- Faint vertical gridlines (#E3E0DC, 1 px) at 520 + 0/130/260/390/520/650 px (i.e. bars
  for 0,1,2,3,4,5 GW — stop at 5 since only Uganda exceeds it).
- Axis numbers 0–5 GW: 16 px weight 400 #8A94A0, aligned below x = 520, 650, 780, 910,
  1040, 1170 at y = 1280.
- No visible axis spine lines.

FOOTER: standard footer, baseline y = 1352.

================================================================================
GRAPHIC 2 — AFRICA'S NUCLEAR MILESTONES, 2015–2026 (vertical timeline)
================================================================================

CANVAS: 2000 x 1500 px, background #FBF9F7.

HEADER BLOCK (top-left at x = 96)
- y=96  : kicker "AFRPOWEROS · OPEN DATA"
- y=142 : H1 "Africa's Nuclear Milestones, 2015–2026"
- y=196 : subtitle "Ten events that trace the continent's civilian nuclear buildout"

TIMELINE SPINE
- Vertical line, x = 1000, from y = 290 to y = 1410, width 3 px, color #16181D.

TEN EVENT ROWS
- Row center y for i=0..9: y = 375 + i*113.
- Marker: 18 px solid circle centered exactly on the spine at (1000, row_center_y),
  colored by the event's status, with a 4 px white ring (stroke #FBF9F7) for contrast.
- Alternate sides: even-index rows draw their card on the LEFT, odd-index rows on the
  RIGHT.
- Card geometry:
  - Left card : x from 340 to 948 (width 608 px).
  - Right card: x from 1052 to 1660 (width 608 px).
  - Vertical: full 96 px tall, vertically centered on row_center_y.
  - A 1 px hairline connector (#E3E0DC) links card edge to the spine marker
    (left card: from card right edge 948 to marker 1000; right: from marker 1000 to
    card left edge 1052).
- Card style: fill #FFFFFF, 2 px border #E3E0DC, corner radius 18 px, inner padding
  22 px left/right, 20 px top/bottom. Content:
  - Line 1 — year label: 26 px weight 700, letter-spacing +0.5 px, in the event's status
    color (e.g. "2015", "Jul 2022", "Oct 2025", "Mar 2026").
  - Line 2 — event text: 19 px weight 450, color #16181D, line-height 1.25, wrapped to
    a maximum of 2 lines.

EVENT DATA (row order, side = card side, year label, text, status color):
  Row 0  LEFT   "2015"  "Russia–Egypt intergovernmental agreement for El Dabaa"
                                       #B85C1C
  Row 1  RIGHT  "2017"  "Ghana completes IAEA Phase 1 milestones"            #1D4ED8
  Row 2  LEFT   "2018"  "Kenya completes IAEA Phase 1 milestones"            #1D4ED8
  Row 3  RIGHT  "2019"  "Uganda and Tanzania complete Phase 1"               #1D4ED8
  Row 4  LEFT   "Jul 2022"  "First concrete poured at El Dabaa Unit 1"       #B85C1C
  Row 5  RIGHT  "Oct 2025"  "South Africa's IRP 2025: 5,200 MW by 2039"      #1B4332
  Row 6  LEFT   "Nov 2025"  "Koeberg Unit 2 operating licence extended to 2045"
                                                                             #1B4332
  Row 7  RIGHT  "Jan 2026"  "DR Congo TRICO-II reactor restart approved"     #A3ACB8
  Row 8  LEFT   "Mar 2026"  "Kenya targets first nuclear generation by 2034" #1D4ED8
  Row 9  RIGHT  "Mar 2026"  "Rwanda completes INIR Phase 2 follow-up"        #1D4ED8

LAYOUT NOTE
- The two "Mar 2026" rows are on opposite sides (Row 8 left, Row 9 right), so their
  cards cannot overlap. Spacing is for legibility, not strict calendar scale.

FOOTER: standard footer, baseline y = 1452.

================================================================================
GRAPHIC 3 — THE CONTINENTAL SCOREBOARD (status overview)
================================================================================

CANVAS: 2000 x 1600 px, background #FBF9F7.

HEADER BLOCK (top-left at x = 96)
- y=96  : kicker "AFRPOWEROS · OPEN DATA"
- y=142 : H1 "The Continental Scoreboard"
- y=196 : subtitle "20 African countries by civilian nuclear program status"

TOTAL CHIP (top-right)
- Pill at x = 1500..1904, y = 96..152: fill #16181D, fully rounded (radius 28 px),
  text centered: "20 COUNTRIES TRACKED" 15 px weight 600, #FFFFFF, uppercase,
  letter-spacing +1.5 px.

FIVE STATUS ROWS
- Row center y for statuses top-to-bottom: 520, 705, 890, 1075, 1260.
- Row composition (all centered on row_center_y):
  - Status name : left at x = 96, 22 px weight 600, color #16181D.
  - Faint track : x = 320 to 1200, height 72 px, #F0ECE6, fully rounded ends.
  - Bar         : x = 320, height 72 px, fully rounded ends (radius 36 px), color and
    width per the table below. Bar width = count x 88 px.
  - Count       : big number 50 px weight 700 color #16181D, placed 40 px to the right
    of the bar end, vertically centered on row_center_y. (e.g. the "10" sits at
    x = 320 + 880 + 40 = 1240.)
  - Country list: 18 px weight 400 color #5C6670, single line below the bar, starting
    at x = 320, y = row_center_y + 62. Wrap onto a second line if longer than the
    canvas; keep text left-aligned.

ROWS (status name | count | bar color | bar width | country text):
  Operating           | 1  | #1B4332 |  88 px | "South Africa — Koeberg"
  Under construction  | 1  | #B85C1C |  88 px | "Egypt — El Dabaa, 4 × VVER-1200"
  Preparing           | 7  | #1D4ED8 | 616 px | "Rwanda, Kenya, Ghana, Uganda,
                        Tanzania, Nigeria, Sudan"
  Exploring           | 10 | #64748B | 880 px | "Zambia, Morocco, Algeria, Ethiopia,
                        Tunisia, Zimbabwe, Senegal, Mali, Niger, Eswatini"
  No program          | 1  | #A3ACB8 |  88 px | "DR Congo — research-reactor restart only"

LAYOUT NOTE
- Bars are deliberately NOT to a shared numeric axis with labels; the count number is
  the primary datum and the bar length is a visual cue proportional to that count.

FOOTER: standard footer, baseline y = 1552.

================================================================================
OUTPUT REQUIREMENTS (all graphics)
================================================================================
- Export each graphic as both JPG (quality 92) and PNG (lossless), 4000 px wide (2x).
- Crisp, clean, editorial. No gradients except the single track/fill pairs specified.
- No extra text, watermarks, logos, or decoration beyond the spec.
- If generating vector code, use the exact hex values and coordinates above.