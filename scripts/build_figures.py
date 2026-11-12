"""Generate 12 calibrated, theme-adaptive `.euclid-graphic` SVG plates for GEOMETOR • apollonius.

All generated SVGs conform to the `.euclid-graphic` contract used by
`photon-platform/publish`'s `.. picture::` directive and `geometor_interactive.js`:
- Adaptive light/dark CSS custom properties (`--geom-fg`, `--geom-bg`, `--geom-accent`, `--geom-assert`)
- `<defs>` midpoint equality tick markers (`#geom-tick-1`, `#geom-tick-2`, `#geom-tick-3`)
- Ordered semantic groups (`#elements`, `#graphics`, `#highlights`, `#points`, `#labels`)
- 3-vertex midpoint straight paths (`M x1 y1 L mx my L x2 y2`) and canonical `data-ref` attributes
"""

from __future__ import annotations

import math
from pathlib import Path

SVG_DEFS_AND_STYLE = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-3.2" y1="-4.5" x2="-3.2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
      <line x1="3.2" y1="-4.5" x2="3.2" y2="4.5" stroke="var(--geom-assert)" stroke-width="1.8" stroke-linecap="round" />
    </marker>
  </defs>
  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-muted: #71717a;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #18181b;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
      --geom-hyper: #2563eb;
      --geom-rose: #be123c;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #e4ded5;
        --geom-bg: #18181b;
        --geom-muted: #a1a1aa;
        --geom-point-stroke: #18181b;
        --geom-poly-fill: #e4ded5;
        --geom-accent: #eab308;
        --geom-assert: #4ade80;
        --geom-hyper: #60a5fa;
        --geom-rose: #fb7185;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', system-ui, sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.75;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.35;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-faint {
      stroke: var(--geom-muted);
      stroke-width: 1.15;
      stroke-opacity: 0.72;
      stroke-linecap: round;
      fill: none;
    }
    .geom-dashed {
      stroke: var(--geom-muted);
      stroke-width: 1.35;
      stroke-dasharray: 5, 3.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-accent-line {
      stroke: var(--geom-accent);
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-assert-line {
      stroke: var(--geom-assert);
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-hyper-line {
      stroke: var(--geom-hyper);
      stroke-width: 2.1;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-rose-line {
      stroke: var(--geom-rose);
      stroke-width: 2.0;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-circle {
      stroke: var(--geom-fg);
      stroke-width: 1.75;
      fill: none;
    }
    .geom-overlay {
      stroke: transparent;
      stroke-width: 4.0;
      stroke-linecap: round;
      fill: none;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.06;
      stroke: none;
    }
    .geom-polygon-accent {
      fill: var(--geom-accent);
      fill-opacity: 0.16;
      stroke: var(--geom-accent);
      stroke-width: 1.4;
    }
    .geom-polygon-assert {
      fill: var(--geom-assert);
      fill-opacity: 0.14;
      stroke: var(--geom-assert);
      stroke-width: 1.4;
    }
    .geom-polygon-rose {
      fill: var(--geom-rose);
      fill-opacity: 0.14;
      stroke: var(--geom-rose);
      stroke-width: 1.4;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.2;
    }
    .geom-point-accent {
      fill: var(--geom-accent);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.2;
    }
    .geom-point-assert {
      fill: var(--geom-assert);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.2;
    }
    .geom-point-rose {
      fill: var(--geom-rose);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.2;
    }
    .geom-label {
      font-size: 13.5px;
      font-weight: 700;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sm {
      font-size: 11.5px;
      font-weight: 700;
      fill: var(--geom-muted);
      user-select: none;
    }
    .geom-label-accent {
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-accent);
      user-select: none;
    }
    .geom-label-assert {
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-assert);
      user-select: none;
    }
    .geom-label-hyper {
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-hyper);
      user-select: none;
    }
    .geom-label-rose {
      font-size: 12.5px;
      font-weight: 700;
      fill: var(--geom-rose);
      user-select: none;
    }
  </style>"""


def _esc_ref(ref: str) -> str:
    return (
        ref.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


class SvgCanvas:
    """Builder for structured `.euclid-graphic` SVG plates."""

    def __init__(self, graphic_id: str, proposition: str, width: int, height: int) -> None:
        self.graphic_id = graphic_id
        self.proposition = proposition
        self.width = width
        self.height = height
        self.elements: list[str] = []
        self.graphics: list[str] = []
        self.highlights: list[str] = []
        self.points: list[str] = []
        self.labels: list[str] = []

    def seg(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        cls: str = "geom-line",
        ref: str | None = None,
        tick: int = 0,
    ) -> None:
        x1, y1 = p1
        x2, y2 = p2
        mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        d = f"M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        tick_attr = f' marker-mid="url(#geom-tick-{tick})"' if tick in (1, 2, 3) else ""
        self.graphics.append(f'    <path d="{d}" class="{cls}"{ref_attr}{tick_attr} />')
        if ref:
            self.highlights.append(f'    <path d="{d}" class="geom-overlay"{ref_attr} />')

    def curve(
        self,
        pts: list[tuple[float, float]],
        cls: str = "geom-bold",
        closed: bool = False,
        ref: str | None = None,
    ) -> None:
        if not pts:
            return
        head = f"M {pts[0][0]:.2f} {pts[0][1]:.2f}"
        rest = " ".join(f"L {x:.2f} {y:.2f}" for x, y in pts[1:])
        end = " Z" if closed else ""
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        self.graphics.append(f'    <path d="{head} {rest}{end}" class="{cls}"{ref_attr} />')

    def circle(
        self,
        center: tuple[float, float],
        r: float,
        cls: str = "geom-circle",
        ref: str | None = None,
    ) -> None:
        cx, cy = center
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        self.graphics.append(
            f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" class="{cls}"{ref_attr} />'
        )
        if ref:
            self.highlights.append(
                f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" class="geom-overlay"{ref_attr} />'
            )

    def ellipse_elem(
        self,
        center: tuple[float, float],
        rx: float,
        ry: float,
        cls: str = "geom-bold",
        angle_deg: float = 0.0,
        ref: str | None = None,
    ) -> None:
        cx, cy = center
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        tr_attr = f' transform="rotate({angle_deg:.2f} {cx:.2f} {cy:.2f})"' if abs(angle_deg) > 1e-6 else ""
        self.graphics.append(
            f'    <ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" '
            f'class="{cls}"{tr_attr}{ref_attr} />'
        )

    def poly(
        self,
        pts: list[tuple[float, float]],
        cls: str = "geom-polygon",
        ref: str | None = None,
    ) -> None:
        s = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        self.elements.append(f'    <polygon points="{s}" class="{cls}"{ref_attr} />')

    def angle_arc(
        self,
        vertex: tuple[float, float],
        p1: tuple[float, float],
        p2: tuple[float, float],
        r: float = 20.0,
        cls: str = "geom-assert-line",
        ref: str | None = None,
    ) -> None:
        vx, vy = vertex
        a1 = math.atan2(p1[1] - vy, p1[0] - vx)
        a2 = math.atan2(p2[1] - vy, p2[0] - vx)
        diff = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
        sweep = 1 if diff >= 0 else 0
        amid = a1 + 0.5 * diff
        sx, sy = vx + r * math.cos(a1), vy + r * math.sin(a1)
        mx, my = vx + r * math.cos(amid), vy + r * math.sin(amid)
        ex, ey = vx + r * math.cos(a2), vy + r * math.sin(a2)
        d = f"M {sx:.2f} {sy:.2f} A {r:.2f} {r:.2f} 0 0 {sweep} {mx:.2f} {my:.2f} A {r:.2f} {r:.2f} 0 0 {sweep} {ex:.2f} {ey:.2f}"
        ref_attr = f' data-ref="{_esc_ref(ref)}"' if ref else ""
        self.graphics.append(f'    <path d="{d}" class="{cls}"{ref_attr} />')

    def right_angle(
        self,
        vertex: tuple[float, float],
        u_dir: tuple[float, float],
        v_dir: tuple[float, float],
        size: float = 9.5,
        cls: str = "geom-faint",
    ) -> None:
        vx, vy = vertex
        un = math.hypot(*u_dir) or 1.0
        vn = math.hypot(*v_dir) or 1.0
        ux, uy = u_dir[0] / un * size, u_dir[1] / un * size
        wx, wy = v_dir[0] / vn * size, v_dir[1] / vn * size
        p1 = (vx + ux, vy + uy)
        p2 = (vx + ux + wx, vy + uy + wy)
        p3 = (vx + wx, vy + wy)
        self.graphics.append(
            f'    <path d="M {p1[0]:.2f} {p1[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f} L {p3[0]:.2f} {p3[1]:.2f}" class="{cls}" />'
        )

    def pt(
        self,
        p: tuple[float, float],
        name: str | None = None,
        offset: tuple[float, float] = (0.0, -10.0),
        cls: str = "geom-point",
        lbl_cls: str = "geom-label",
        ref: str | None = None,
        r: float = 3.4,
    ) -> None:
        x, y = p
        actual_ref = ref or (name if name and name.isalnum() else None)
        ref_attr = f' data-ref="{_esc_ref(actual_ref)}"' if actual_ref else ""
        self.points.append(
            f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" class="{cls}"{ref_attr} />'
        )
        if name:
            self.lbl((x + offset[0], y + offset[1]), name, cls=lbl_cls)

    def lbl(
        self,
        p: tuple[float, float],
        text: str,
        cls: str = "geom-label",
        anchor: str = "middle",
    ) -> None:
        self.labels.append(
            f'    <text x="{p[0]:.2f}" y="{p[1]:.2f}" text-anchor="{anchor}" class="{cls}">{_esc_ref(text)}</text>'
        )

    def render(self) -> str:
        header = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}" class="euclid-graphic" '
            f'data-graphic-id="{self.graphic_id}" data-proposition="{self.proposition}">'
        )
        lines = [
            header,
            SVG_DEFS_AND_STYLE,
            '  <g id="elements">',
            *self.elements,
            "  </g>",
            '  <g id="graphics">',
            *self.graphics,
            "  </g>",
            '  <g id="highlights" style="pointer-events: none;">',
            *self.highlights,
            "  </g>",
            '  <g id="points">',
            *self.points,
            "  </g>",
            '  <g id="labels">',
            *self.labels,
            "  </g>",
            "</svg>",
            "",
        ]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Plate 1: Oblique Scalene Double Cone, Subcontrary Circle & 3 Conic Sections
# ---------------------------------------------------------------------------
def fig_oblique_cone_sections() -> str:
    """Book I.1–14: Oblique scalene double cone, axial triangle, subcontrary circle & 3 conics."""
    svg = SvgCanvas("g1", "I.1-14", 760, 360)

    # Left panel: Oblique double cone with axial triangle and 3 conic planes
    a = (210.0, 142.0)  # Apex A (skewed left relative to lower base center -> scalene!)
    b_low, c_low = (96.0, 312.0), (392.0, 312.0)
    o_low = (0.5 * (b_low[0] + c_low[0]), 312.0)
    # Upper nappe generators extending above A along lines BA and CA:
    # A + t*(A - B_low) and A + t*(A - C_low), t = 0.58
    t_up = 0.62
    b_up = (a[0] + t_up * (a[0] - c_low[0]), a[1] + t_up * (a[1] - c_low[1]))
    c_up = (a[0] + t_up * (a[0] - b_low[0]), a[1] + t_up * (a[1] - b_low[1]))
    o_up = (0.5 * (b_up[0] + c_up[0]), 0.5 * (b_up[1] + c_up[1]))

    svg.lbl((235, 22), "I.1–14: Single Oblique Double Cone & Three Sections", "geom-label-sm")
    svg.poly([a, b_low, c_low], "geom-polygon", ref="< A B C >")
    svg.poly([a, b_up, c_up], "geom-polygon")

    # Circular bases projected obliquely
    svg.ellipse_elem(o_low, 0.5 * (c_low[0] - b_low[0]), 24.0, "geom-line")
    svg.ellipse_elem(o_up, 0.5 * (c_up[0] - b_up[0]), 15.0, "geom-dashed")

    # Oblique axis O_up - A - O_low
    svg.seg(o_up, o_low, "geom-dashed", ref="[ A O ]")
    # Generators B_low - A - C_up and C_low - A - B_up
    svg.seg(b_low, c_up, "geom-bold", ref="[ A B ]")
    svg.seg(c_low, b_up, "geom-bold", ref="[ A C ]")
    svg.seg(b_low, c_low, "geom-faint", ref="/ B C /")

    # 1. Ellipse section cutting both generators AB and AC on lower nappe
    e1 = (a[0] + 0.44 * (b_low[0] - a[0]), a[1] + 0.44 * (b_low[1] - a[1]))
    e2 = (a[0] + 0.62 * (c_low[0] - a[0]), a[1] + 0.62 * (c_low[1] - a[1]))
    emid = (0.5 * (e1[0] + e2[0]), 0.5 * (e1[1] + e2[1]))
    ehalf = 0.5 * math.hypot(e2[0] - e1[0], e2[1] - e1[1])
    eang = math.degrees(math.atan2(e2[1] - e1[1], e2[0] - e1[0]))
    svg.ellipse_elem(emid, ehalf, 14.0, "geom-assert-line", angle_deg=eang)
    svg.seg(e1, e2, "geom-assert-line", ref="/ E1 E2 /")

    # 2. Parabola section parallel to generator AC: vertex P1 on AB, extending to base BC
    p_v = (a[0] + 0.68 * (b_low[0] - a[0]), a[1] + 0.68 * (b_low[1] - a[1]))
    # Parallel to AC meets BC at M_p where P_v + s*(c_low - a) has y = 312
    s_p = (312.0 - p_v[1]) / (c_low[1] - a[1])
    m_p = (p_v[0] + s_p * (c_low[0] - a[0]), 312.0)
    para_pts: list[tuple[float, float]] = []
    for k in range(-18, 19):
        u = k / 18.0
        # Parameterize parabolic arch on base chord around m_p with vertex p_v
        t_par = u * u
        cx_p = p_v[0] + t_par * (m_p[0] - p_v[0]) - 22.0 * u * 0.45
        cy_p = p_v[1] + t_par * (m_p[1] - p_v[1]) + 15.0 * u * 0.55
        para_pts.append((cx_p, cy_p))
    svg.curve(para_pts, "geom-accent-line")
    svg.seg(p_v, m_p, "geom-accent-line", ref="/ P M /")

    # 3. Hyperbola section cutting upper nappe at H2 and lower nappe at H1
    h1 = (a[0] + 0.48 * (c_low[0] - a[0]), a[1] + 0.48 * (c_low[1] - a[1]))
    h2 = (a[0] + 0.42 * (b_up[0] - a[0]), a[1] + 0.42 * (b_up[1] - a[1]))
    svg.seg((h2[0] + 6, 36.0), (h1[0] + 22, 334.0), "geom-hyper-line", ref="[ H1 H2 ]")
    hyp_low = [
        (h1[0] + 22 * u * u - 10 * u, h1[1] + (332 - h1[1]) * u * u + 8 * u)
        for u in [k / 14.0 for k in range(-14, 15)]
    ]
    hyp_up = [
        (h2[0] - 16 * u * u - 8 * u, h2[1] - (h2[1] - 38) * u * u + 6 * u)
        for u in [k / 14.0 for k in range(-14, 15)]
    ]
    svg.curve(hyp_low, "geom-hyper-line")
    svg.curve(hyp_up, "geom-hyper-line")

    svg.pt(a, "A", (-13, -4))
    svg.pt(b_low, "B", (-12, 6))
    svg.pt(c_low, "C", (12, 6))
    svg.pt(o_low, "O", (0, 17), lbl_cls="geom-label-sm")
    svg.pt(e1, "E₁", (-15, -2), "geom-point-assert", "geom-label-assert", ref="E1")
    svg.pt(e2, "E₂", (16, -2), "geom-point-assert", "geom-label-assert", ref="E2")
    svg.pt(p_v, "P", (-14, 4), "geom-point-accent", "geom-label-accent", ref="P")
    svg.pt(h1, "H₁", (16, 2), cls="geom-point", lbl_cls="geom-label-hyper", ref="H1")
    svg.pt(h2, "H₂", (-16, 4), cls="geom-point", lbl_cls="geom-label-hyper", ref="H2")

    svg.lbl((64, 212), "Ellipse", "geom-label-assert")
    svg.lbl((66, 268), "Parabola (∥ AC)", "geom-label-accent")
    svg.lbl((348, 86), "Hyperbola (2 branches)", "geom-label-hyper")

    # Right panel: Subcontrary (antiparallel) circular section I.5
    svg.seg((436, 20), (436, 340), "geom-faint")
    svg.lbl((596, 22), "I.5: Subcontrary Circular Section", "geom-label-sm")

    sa = (562.0, 56.0)
    sb = (468.0, 298.0)
    sc = (722.0, 298.0)
    svg.poly([sa, sb, sc], "geom-polygon")
    svg.seg(sa, sb, "geom-bold", ref="/ SA SB /")
    svg.seg(sa, sc, "geom-bold", ref="/ SA SC /")
    svg.seg(sb, sc, "geom-line", ref="/ SB SC /")

    # Exact antiparallel condition: triangle AKG ~ triangle ACB -> AK/AC = AG/AB = lam
    ab_len = math.hypot(sb[0] - sa[0], sb[1] - sa[1])
    ac_len = math.hypot(sc[0] - sa[0], sc[1] - sa[1])
    ak_len = 152.0
    ag_len = ak_len * ab_len / ac_len
    sk = (
        sa[0] + ak_len / ab_len * (sb[0] - sa[0]),
        sa[1] + ak_len / ab_len * (sb[1] - sa[1]),
    )
    sg = (
        sa[0] + ag_len / ac_len * (sc[0] - sa[0]),
        sa[1] + ag_len / ac_len * (sc[1] - sa[1]),
    )

    # Point M on KG and parallel section DME || BC
    sm = (0.46 * sk[0] + 0.54 * sg[0], 0.46 * sk[1] + 0.54 * sg[1])
    t_par_bc = (sm[1] - sa[1]) / (sb[1] - sa[1])
    sd = (sa[0] + t_par_bc * (sb[0] - sa[0]), sm[1])
    se = (sa[0] + t_par_bc * (sc[0] - sa[0]), sm[1])

    svg.seg(sd, se, "geom-dashed", ref="/ D E /")
    svg.seg(sk, sg, "geom-accent-line", ref="/ K G /")

    # Folded semicircle on KG showing PM^2 = KM * MG = DM * ME
    kg_mid = (0.5 * (sk[0] + sg[0]), 0.5 * (sk[1] + sg[1]))
    kg_rad = 0.5 * math.hypot(sg[0] - sk[0], sg[1] - sk[1])
    kg_dir = ((sg[0] - sk[0]) / (2 * kg_rad), (sg[1] - sk[1]) / (2 * kg_rad))
    n_perp = (kg_dir[1], -kg_dir[0])  # upward normal to KG
    km_len = math.hypot(sm[0] - sk[0], sm[1] - sk[1])
    mg_len = math.hypot(sg[0] - sm[0], sg[1] - sm[1])
    pm_len = math.sqrt(km_len * mg_len)
    sp = (sm[0] + pm_len * n_perp[0], sm[1] + pm_len * n_perp[1])

    semi_pts = []
    ang0 = math.atan2(sk[1] - kg_mid[1], sk[0] - kg_mid[0])
    for j in range(37):
        th = ang0 + math.pi * j / 36.0
        # ensure arc goes on same side as sp
        px = kg_mid[0] + kg_rad * math.cos(th)
        py = kg_mid[1] + kg_rad * math.sin(th)
        if (px - kg_mid[0]) * n_perp[0] + (py - kg_mid[1]) * n_perp[1] < -1e-6:
            th = ang0 - math.pi * j / 36.0
            px = kg_mid[0] + kg_rad * math.cos(th)
            py = kg_mid[1] + kg_rad * math.sin(th)
        semi_pts.append((px, py))
    svg.curve(semi_pts, "geom-assert-line")
    svg.seg(sm, sp, "geom-assert-line", ref="/ M P1 /")
    svg.right_angle(sm, kg_dir, n_perp, 8.0)

    # Matching angle arcs: <AKG = <ACB
    svg.angle_arc(sk, sa, sg, 18.0, "geom-assert-line", ref="< SA K G )")
    svg.angle_arc(sc, sb, sa, 22.0, "geom-assert-line", ref="< SB SC SA )")

    svg.pt(sa, "A", (0, -10))
    svg.pt(sb, "B", (-12, 6))
    svg.pt(sc, "C", (12, 6))
    svg.pt(sk, "K", (-14, -2), "geom-point-accent", "geom-label-accent")
    svg.pt(sg, "G", (14, 2), "geom-point-accent", "geom-label-accent")
    svg.pt(sd, "D", (-13, 4), lbl_cls="geom-label-sm")
    svg.pt(se, "E", (13, 4), lbl_cls="geom-label-sm")
    svg.pt(sm, "M", (2, 16), lbl_cls="geom-label-sm")
    svg.pt(sp, "P", (0, -10), "geom-point-assert", "geom-label-assert")
    svg.lbl((596, 334), "∠AKG = ∠ACB  ⇒  PM² = DM·ME = KM·MG", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 2: Application of Areas (Parabole, Elleipsis, Hyperbole) — I.11–13
# ---------------------------------------------------------------------------
def fig_application_of_areas() -> str:
    """Book I.11–13: Exact, Deficient & Exceeding Application of Areas on Latus Rectum p."""
    svg = SvgCanvas("g2", "I.11-13", 780, 320)

    # Panel 1: PARABOLA (y^2 = p x)
    svg.lbl((130, 22), "I.11: Parabola (παραβολή)", "geom-label-accent")
    svg.lbl((130, 39), "Exact Application: QV² = PL · PV = p x", "geom-label-sm")
    p1 = (66.0, 184.0)
    p_par = 64.0
    x_par = 86.0
    y_par = math.sqrt(p_par * x_par)
    v1 = (p1[0] + x_par, p1[1])
    l1 = (p1[0], p1[1] + p_par)
    r1 = (v1[0], p1[1] + p_par)
    q1 = (v1[0], p1[1] - y_par)

    # Applied rectangle PV * PL (exact equality, no defect/excess)
    svg.poly([p1, v1, r1, l1], "geom-polygon-accent", ref="< P1 V1 R1 L1 >")
    svg.seg((46, p1[1]), (226, p1[1]), "geom-line")
    svg.seg(p1, l1, "geom-accent-line", ref="/ P1 L1 /")
    svg.seg(v1, q1, "geom-bold", ref="/ V1 Q1 /")
    par_curve = [
        (p1[0] + u, p1[1] - math.sqrt(p_par * u))
        for u in [k * 3.5 for k in range(44)]
    ]
    svg.curve(par_curve, "geom-bold")
    svg.pt(p1, "P", (-11, -6))
    svg.pt(v1, "V", (10, -5))
    svg.pt(q1, "Q", (12, -4), "geom-point-accent")
    svg.pt(l1, "L", (-12, 5), "geom-point-accent", "geom-label-accent")
    svg.lbl((51, p1[1] + 36), "p", "geom-label-accent")
    svg.lbl((p1[0] + 0.5 * x_par, p1[1] + 36), "p x", "geom-label-accent")
    svg.lbl((v1[0] + 13, p1[1] - 0.5 * y_par), "y", "geom-label-sm")

    # Divider 1
    svg.seg((252, 18), (252, 302), "geom-faint")

    # Panel 2: ELLIPSE (y^2 = p x - (p/d) x^2)
    svg.lbl((390, 22), "I.12: Ellipse (ἔλλειψις)", "geom-label-assert")
    svg.lbl((390, 39), "Defect: QV² = x(p − p x / d)", "geom-label-sm")
    p2 = (284.0, 184.0)
    d_ell = 186.0
    p_ell = 76.0
    x_ell = 68.0
    p2_prime = (p2[0] + d_ell, p2[1])
    v2 = (p2[0] + x_ell, p2[1])
    l2 = (p2[0], p2[1] + p_ell)
    # Line P'L determines VR = p * (1 - x/d)
    vr_ell = p_ell * (1.0 - x_ell / d_ell)
    y_ell = math.sqrt(x_ell * vr_ell)
    q2 = (v2[0], p2[1] - y_ell)
    r2 = (v2[0], p2[1] + vr_ell)
    m2 = (p2[0], p2[1] + vr_ell)
    full2 = (v2[0], p2[1] + p_ell)

    # Applied rectangle PV * PM (= y^2) in green + Defect rectangle (falls short!) in rose
    svg.poly([p2, v2, r2, m2], "geom-polygon-assert", ref="< P2 V2 R2 M2 >")
    svg.poly([m2, r2, full2, l2], "geom-polygon-rose", ref="< M2 R2 F2 L2 >")
    svg.seg((268, p2[1]), (488, p2[1]), "geom-line")
    svg.seg(p2, l2, "geom-accent-line", ref="/ P2 L2 /")
    svg.seg(p2_prime, l2, "geom-dashed", ref="/ P2p L2 /")
    svg.seg(v2, q2, "geom-bold", ref="/ V2 Q2 /")
    ell_curve = [
        (p2[0] + u, p2[1] - math.sqrt(max(0.0, p_ell * u - (p_ell / d_ell) * u * u)))
        for u in [d_ell * k / 60.0 for k in range(61)]
    ]
    svg.curve(ell_curve, "geom-bold")
    svg.pt(p2, "P", (-10, -6))
    svg.pt(p2_prime, "P′", (11, -6))
    svg.pt(v2, "V", (9, -5))
    svg.pt(q2, "Q", (0, -10), "geom-point-assert")
    svg.pt(l2, "L", (-11, 5), "geom-point-accent", "geom-label-accent")
    svg.pt(r2, "R", (11, 4), "geom-point-rose", "geom-label-rose")
    svg.lbl((p2[0] + 0.5 * x_ell, p2[1] + 0.52 * vr_ell + 4), "y²", "geom-label-assert")
    svg.lbl((p2[0] + 0.5 * x_ell, p2[1] + 0.5 * (vr_ell + p_ell) + 4), "defect", "geom-label-rose")

    # Divider 2
    svg.seg((508, 18), (508, 302), "geom-faint")

    # Panel 3: HYPERBOLA (y^2 = p x + (p/d) x^2)
    svg.lbl((644, 22), "I.13: Hyperbola (ὑπερβολή)", "geom-label-hyper")
    svg.lbl((644, 39), "Excess: QV² = x(p + p x / d)", "geom-label-sm")
    p3_prime = (534.0, 184.0)
    d_hyp = 92.0
    p3 = (p3_prime[0] + d_hyp, 184.0)
    p_hyp = 56.0
    x_hyp = 64.0
    v3 = (p3[0] + x_hyp, p3[1])
    l3 = (p3[0], p3[1] + p_hyp)
    vr_hyp = p_hyp * (1.0 + x_hyp / d_hyp)
    y_hyp = math.sqrt(x_hyp * vr_hyp)
    q3 = (v3[0], p3[1] - y_hyp)
    full3 = (v3[0], p3[1] + p_hyp)
    r3 = (v3[0], p3[1] + vr_hyp)
    m3 = (p3[0], p3[1] + vr_hyp)

    # Base rectangle p*x in accent + Excess rectangle (p/d)*x^2 beyond L in hyper/rose
    svg.poly([p3, v3, full3, l3], "geom-polygon-accent", ref="< P3 V3 F3 L3 >")
    svg.poly([l3, full3, r3, m3], "geom-polygon-assert", ref="< L3 F3 R3 M3 >")
    svg.seg((520, p3[1]), (762, p3[1]), "geom-line")
    svg.seg(p3, m3, "geom-dashed")
    svg.seg(p3, l3, "geom-accent-line", ref="/ P3 L3 /")
    svg.seg(p3_prime, r3, "geom-dashed", ref="/ P3p R3 /")
    svg.seg(v3, q3, "geom-bold", ref="/ V3 Q3 /")
    hyp_curve = [
        (p3[0] + u, p3[1] - math.sqrt(p_hyp * u + (p_hyp / d_hyp) * u * u))
        for u in [3.0 * k for k in range(34)]
    ]
    svg.curve(hyp_curve, "geom-bold")
    svg.pt(p3_prime, "P′", (-8, -7))
    svg.pt(p3, "P", (-8, -7))
    svg.pt(v3, "V", (9, -5))
    svg.pt(q3, "Q", (-11, -5), "geom-point-accent")
    svg.pt(l3, "L", (-11, 3), "geom-point-accent", "geom-label-accent")
    svg.pt(r3, "R", (12, 4), "geom-point-assert", "geom-label-assert")
    svg.lbl((p3[0] + 0.5 * x_hyp, p3[1] + 0.52 * p_hyp + 4), "p x", "geom-label-accent")
    svg.lbl((p3[0] + 0.5 * x_hyp, p3[1] + 0.5 * (p_hyp + vr_hyp) + 4), "excess", "geom-label-assert")
    svg.lbl((0.5 * (p3_prime[0] + p3[0]), p3[1] + 18), "d", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 3: Tangent & Harmonic Division of the Diameter — I.33–37
# ---------------------------------------------------------------------------
def fig_tangent_harmonic_division() -> str:
    """Book I.33–37: Tangent PT, ordinate PV, harmonic range (A', A; V, T) = -1 & CV·CT = CA²."""
    svg = SvgCanvas("g3", "I.33-37", 680, 320)
    cx, cy = 245.0, 178.0
    a, b = 128.0, 84.0

    # Choose P at x0 = a / 2 = 64 -> x_T = a^2 / x0 = 2a = 256! Exact rational abscissae!
    x0 = 0.5 * a
    y0 = b * math.sqrt(1.0 - (x0 / a) ** 2)
    xt = a * a / x0  # = 256.0

    p_c = (cx, cy)
    p_ap = (cx - a, cy)
    p_a = (cx + a, cy)
    p_v = (cx + x0, cy)
    p_p = (cx + x0, cy - y0)
    p_t = (cx + xt, cy)

    # Conjugate semi-diameter CD parallel to tangent PT: eccentric angle theta + pi/2
    # P = (a cos th, -b sin th) in SVG coords -> D = (-a sin th, -b cos th)
    sin_th = math.sqrt(1.0 - (x0 / a) ** 2)
    cos_th = x0 / a
    p_d = (cx - a * sin_th, cy - b * cos_th)
    p_dp = (cx + a * sin_th, cy + b * cos_th)

    svg.lbl((340, 24), "I.34–37: Harmonic Tangent Construction  (A′, A ; V, T) = −1  &  CV · CT = CA²", "geom-label-sm")
    svg.ellipse_elem(p_c, a, b, "geom-bold", ref="( C A )")
    svg.seg((48, cy), (636, cy), "geom-line", ref="[ A1 A ]")
    svg.seg(p_dp, p_d, "geom-dashed", ref="/ D1 D /")
    svg.seg(p_p, p_v, "geom-assert-line", ref="/ P V /")
    svg.seg(p_p, p_t, "geom-accent-line", ref="/ P T /")
    svg.right_angle(p_v, (-1, 0), (0, -1), 9.0)

    # Harmonic arcs / ratio callout underneath axis
    svg.seg((p_ap[0], cy + 44), (p_t[0], cy + 44), "geom-faint")
    for px in (p_ap[0], p_c[0], p_v[0], p_a[0], p_t[0]):
        svg.seg((px, cy + 38), (px, cy + 50), "geom-faint")
    svg.lbl((0.5 * (p_ap[0] + p_v[0]), cy + 64), "A′V = 3a/2", "geom-label-sm")
    svg.lbl((0.5 * (p_v[0] + p_a[0]), cy + 64), "VA = a/2", "geom-label-assert")
    svg.lbl((0.5 * (p_a[0] + p_t[0]), cy + 64), "AT = a", "geom-label-accent")
    svg.lbl((340, 294), "A′V : VA = 3 : 1 = A′T : TA   (Harmonic Conjugate T of V wrt A′A)", "geom-label-sm")

    svg.pt(p_ap, "A′", (-14, -8), ref="A1")
    svg.pt(p_c, "C", (-8, 18))
    svg.pt(p_v, "V", (-8, 18), "geom-point-assert", "geom-label-assert")
    svg.pt(p_a, "A", (10, -8))
    svg.pt(p_t, "T", (0, -11), "geom-point-accent", "geom-label-accent")
    svg.pt(p_p, "P", (6, -11), "geom-point-accent", "geom-label-accent")
    svg.pt(p_d, "D", (-12, -8), lbl_cls="geom-label-sm")
    svg.lbl((p_t[0] - 85, p_p[1] + 24), "tangent PT ∥ CD", "geom-label-accent")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 4: Hyperbola, Asymptotes, Conjugate Hyperbola & Secant Intercepts — II.1–17
# ---------------------------------------------------------------------------
def fig_hyperbola_asymptotes_secant() -> str:
    """Book II.1–17: Primary & conjugate hyperbolas, asymptotes, bisected tangent & RQ = Q'R'."""
    svg = SvgCanvas("g4", "II.1-17", 680, 380)
    cx, cy = 340.0, 196.0
    a, b = 78.0, 54.0

    svg.lbl((340, 22), "II.1–17: Asymptotes, Conjugate Hyperbolas, Tangent Bisection & Equal Secant Intercepts", "geom-label-sm")

    # Asymptotes y = +/- (b/a) x
    dx_asym = 278.0
    dy_asym = (b / a) * dx_asym
    svg.seg((cx - dx_asym, cy - dy_asym), (cx + dx_asym, cy + dy_asym), "geom-dashed", ref="[ L1 L2 ]")
    svg.seg((cx - dx_asym, cy + dy_asym), (cx + dx_asym, cy - dy_asym), "geom-dashed", ref="[ M1 M2 ]")

    # Primary hyperbola x^2/a^2 - y^2/b^2 = 1 (left & right branches)
    right_br = [(cx + a * math.cosh(t), cy - b * math.sinh(t)) for t in [k * 0.08 for k in range(-22, 23)]]
    left_br = [(cx - a * math.cosh(t), cy - b * math.sinh(t)) for t in [k * 0.08 for k in range(-22, 23)]]
    svg.curve(right_br, "geom-bold")
    svg.curve(left_br, "geom-bold")

    # Conjugate hyperbola y^2/b^2 - x^2/a^2 = 1 (top & bottom branches)
    top_br = [(cx + a * math.sinh(t), cy - b * math.cosh(t)) for t in [k * 0.08 for k in range(-21, 22)]]
    bot_br = [(cx + a * math.sinh(t), cy + b * math.cosh(t)) for t in [k * 0.08 for k in range(-21, 22)]]
    svg.curve(top_br, "geom-hyper-line")
    svg.curve(bot_br, "geom-hyper-line")

    # Exact tangent at P(a cosh t0, -b sinh t0) terminated by asymptotes at D, D':
    # In math coords: P = (a cosh t0, b sinh t0). Tangent x cosh t0 / a - y sinh t0 / b = 1.
    # Meets y = +(b/a)x at x = a / (cosh t0 - sinh t0) = a e^{t0} -> D1 = (a e^{t0}, b e^{t0})
    # Meets y = -(b/a)x at x = a / (cosh t0 + sinh t0) = a e^{-t0} -> D2 = (a e^{-t0}, -b e^{-t0})
    # Note midpoint of D1 and D2 is EXACTLY P! (Apollonius II.3!)
    t0 = 0.52
    ep, em = math.exp(t0), math.exp(-t0)
    p_pt = (cx + a * math.cosh(t0), cy - b * math.sinh(t0))
    d1 = (cx + a * ep, cy - b * ep)
    d2 = (cx + a * em, cy + b * em)
    svg.seg(d1, p_pt, "geom-accent-line", ref="/ D1 P /", tick=1)
    svg.seg(p_pt, d2, "geom-accent-line", ref="/ P D2 /", tick=1)

    # Exact secant cutting right branch in two points Q, Q' and asymptotes in R, R' (Apollonius II.8):
    # In math coords: line x - m*y = k with |m| < a/b cuts right branch in Q, Q' and asymptotes y = +/-(b/a)x in R, R'!
    # Let m = 0.82 * (a / b) * 0.48, k = 1.48 * a:
    m_sec = 0.52
    k_sec = 1.58 * a
    # Solve (k + m y)^2 / a^2 - y^2 / b^2 = 1 -> (m^2/a^2 - 1/b^2) y^2 + (2 k m / a^2) y + (k^2/a^2 - 1) = 0
    qa = m_sec * m_sec / (a * a) - 1.0 / (b * b)
    qb = 2.0 * k_sec * m_sec / (a * a)
    qc = k_sec * k_sec / (a * a) - 1.0
    disc = math.sqrt(qb * qb - 4.0 * qa * qc)
    yq1 = (-qb - disc) / (2.0 * qa)  # positive y
    yq2 = (-qb + disc) / (2.0 * qa)  # negative y
    xq1, xq2 = k_sec + m_sec * yq1, k_sec + m_sec * yq2
    # Intersections with asymptotes x = +/-(a/b) y:
    yr1 = k_sec / (a / b - m_sec)
    xr1 = (a / b) * yr1
    yr2 = k_sec / (-a / b - m_sec)
    xr2 = -(a / b) * yr2

    p_r1 = (cx + xr1, cy - yr1)
    p_q1 = (cx + xq1, cy - yq1)
    p_q2 = (cx + xq2, cy - yq2)
    p_r2 = (cx + xr2, cy - yr2)

    svg.seg(p_q1, p_q2, "geom-line", ref="/ Q1 Q2 /")
    svg.seg(p_r1, p_q1, "geom-assert-line", ref="/ R1 Q1 /", tick=2)
    svg.seg(p_q2, p_r2, "geom-assert-line", ref="/ Q2 R2 /", tick=2)

    svg.pt((cx, cy), "C", (-12, 4))
    svg.pt((cx + a, cy), "A", (-10, 14), lbl_cls="geom-label-sm")
    svg.pt((cx - a, cy), "A′", (10, 14), lbl_cls="geom-label-sm")
    svg.pt(p_pt, "P", (-12, -5), "geom-point-accent", "geom-label-accent")
    svg.pt(d1, "D", (-10, -8), "geom-point-accent", "geom-label-accent")
    svg.pt(d2, "D′", (-12, 12), "geom-point-accent", "geom-label-accent")
    svg.pt(p_r1, "R", (13, -4), "geom-point-assert", "geom-label-assert")
    svg.pt(p_q1, "Q", (13, 3), "geom-point-assert", "geom-label-assert")
    svg.pt(p_q2, "Q′", (14, 3), "geom-point-assert", "geom-label-assert")
    svg.pt(p_r2, "R′", (14, 10), "geom-point-assert", "geom-label-assert")

    svg.lbl((cx, 62), "Conjugate Hyperbola", "geom-label-hyper")
    svg.lbl((122, 198), "Opposite Branch", "geom-label-sm")
    svg.lbl((340, 364), "II.3: DP = PD′ (tangent bisected)   ·   II.8: RQ = Q′R′ (secant intercepts equal)", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 5: Harmonic Pole & Polar Duality — III.37–40
# ---------------------------------------------------------------------------
def fig_harmonic_pole_polar() -> str:
    """Book III.37–40: Pole T, tangents TP1 & TP2, polar P1P2 & harmonic secants (T, R; A, B) = -1."""
    svg = SvgCanvas("g5", "III.37-40", 680, 340)
    cx, cy = 415.0, 182.0
    a, b = 156.0, 98.0

    # External pole T in math coords relative to C (y up):
    tx, ty = -295.0, 38.0

    # Polar line: (tx/a^2) x + (ty/b^2) y = 1. Intersect with x^2/a^2 + y^2/b^2 = 1:
    alpha = tx / (a * a)
    beta = ty / (b * b)
    # x = (1 - beta y) / alpha -> ((1 - beta y)^2)/(alpha^2 a^2) + y^2/b^2 = 1
    qa = (beta * beta) / (alpha * alpha * a * a) + 1.0 / (b * b)
    qb = -2.0 * beta / (alpha * alpha * a * a)
    qc = 1.0 / (alpha * alpha * a * a) - 1.0
    disc = math.sqrt(qb * qb - 4.0 * qa * qc)
    yp1 = (-qb + disc) / (2.0 * qa)
    yp2 = (-qb - disc) / (2.0 * qa)
    xp1 = (1.0 - beta * yp1) / alpha
    xp2 = (1.0 - beta * yp2) / alpha

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx + mx, cy - my)

    def secant_hits(slope: float) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        # Ray from (tx, ty) with direction (1, slope): (tx + u, ty + slope*u)
        sa = 1.0 / (a * a) + (slope * slope) / (b * b)
        sb = 2.0 * (tx / (a * a) + ty * slope / (b * b))
        sc = (tx * tx) / (a * a) + (ty * ty) / (b * b) - 1.0
        sd = math.sqrt(sb * sb - 4.0 * sa * sc)
        u1 = (-sb - sd) / (2.0 * sa)
        u2 = (-sb + sd) / (2.0 * sa)
        # Polar intersection: alpha*(tx + ur) + beta*(ty + slope*ur) = 1
        ur = (1.0 - (alpha * tx + beta * ty)) / (alpha + beta * slope)
        return (
            to_svg(tx + u1, ty + slope * u1),
            to_svg(tx + ur, ty + slope * ur),
            to_svg(tx + u2, ty + slope * u2),
        )

    p_t = to_svg(tx, ty)
    p_p1 = to_svg(xp1, yp1)
    p_p2 = to_svg(xp2, yp2)
    p_a, p_r, p_b = secant_hits(-0.04)
    p_g, p_s, p_h = secant_hits(-0.23)

    svg.lbl((340, 22), "III.37–40: Harmonic Pole & Polar Duality  (T, R ; A, B) = −1  &  (T, S ; G, H) = −1", "geom-label-sm")
    svg.ellipse_elem((cx, cy), a, b, "geom-bold")

    # Tangents from Pole T
    svg.seg(p_t, p_p1, "geom-accent-line", ref="/ T P1 /")
    svg.seg(p_t, p_p2, "geom-accent-line", ref="/ T P2 /")

    # Extended Polar line through P1, P2
    pdir = (p_p2[0] - p_p1[0], p_p2[1] - p_p1[1])
    svg.seg(
        (p_p1[0] - 0.16 * pdir[0], p_p1[1] - 0.16 * pdir[1]),
        (p_p2[0] + 0.18 * pdir[0], p_p2[1] + 0.18 * pdir[1]),
        "geom-rose-line",
        ref="[ P1 P2 ]",
    )

    # Complete quadrangle diagonals AG x BH and AH x BG (meeting on the polar!)
    svg.seg(p_a, p_h, "geom-faint")
    svg.seg(p_b, p_g, "geom-faint")

    # Two harmonic secants
    svg.seg(p_t, p_b, "geom-assert-line", ref="/ T B /")
    svg.seg(p_t, p_h, "geom-hyper-line", ref="/ T H /")

    svg.pt(p_t, "T (Pole)", (8, -12), "geom-point-accent", "geom-label-accent", ref="T")
    svg.pt(p_p1, "P₁", (0, -11), "geom-point-rose", "geom-label-rose", ref="P1")
    svg.pt(p_p2, "P₂", (2, 18), "geom-point-rose", "geom-label-rose", ref="P2")
    svg.pt(p_a, "A", (-6, -10), "geom-point-assert", "geom-label-assert")
    svg.pt(p_r, "R", (10, -9), "geom-point-rose", "geom-label-rose")
    svg.pt(p_b, "B", (12, -6), "geom-point-assert", "geom-label-assert")
    svg.pt(p_g, "G", (-8, 16), lbl_cls="geom-label-hyper")
    svg.pt(p_s, "S", (11, 14), "geom-point-rose", "geom-label-rose")
    svg.pt(p_h, "H", (13, 8), lbl_cls="geom-label-hyper")

    svg.lbl((p_p1[0] - 48, p_p1[1] + 46), "Polar P₁P₂", "geom-label-rose")
    svg.lbl((340, 324), "TA : TB = AR : RB   and   TG : TH = GS : SH   (Projective Harmonic Polarity)", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 6: Central Conic Foci, Auxiliary Pedal Circle & PF1 + PF2 = 2a — III.45–52
# ---------------------------------------------------------------------------
def fig_central_conic_foci() -> str:
    """Book III.45–52: Foci F1, F2, tangent angle bisection, pedal circle & PF1 + PF2 = 2a."""
    svg = SvgCanvas("g6", "III.45-52", 680, 360)
    cx, cy = 340.0, 192.0
    a, b = 152.0, 102.0
    c = math.sqrt(a * a - b * b)

    # Point P on ellipse at eccentric angle th
    th = 0.92
    px, py = a * math.cos(th), b * math.sin(th)  # math coords (y up)
    # Tangent at P: (cos th / a) x + (sin th / b) y = 1
    # Intersects vertex tangent x = +a at K:
    yk_right = b * (1.0 - math.cos(th)) / math.sin(th)

    # Feet Z1, Z2 of perpendiculars from F1(-c,0), F2(+c,0) onto tangent:
    # Normal vector n = (cos th / a, sin th / b)
    nx, ny = math.cos(th) / a, math.sin(th) / b
    n2 = nx * nx + ny * ny

    def foot_on_tangent(fx: float, fy: float) -> tuple[float, float]:
        lam = (1.0 - (nx * fx + ny * fy)) / n2
        return (fx + lam * nx, fy + lam * ny)

    z1x, z1y = foot_on_tangent(-c, 0.0)
    z2x, z2y = foot_on_tangent(c, 0.0)

    def S(mx: float, my: float) -> tuple[float, float]:
        return (cx + mx, cy - my)

    p_c = S(0, 0)
    p_ap, p_a = S(-a, 0), S(a, 0)
    p_f1, p_f2 = S(-c, 0), S(c, 0)
    p_p = S(px, py)
    p_k = S(a, yk_right)
    p_z1, p_z2 = S(z1x, z1y), S(z2x, z2y)

    svg.lbl((340, 22), "III.45–52: Foci (AF₁ · F₁A′ = b²), Auxiliary Pedal Circle & PF₁ + PF₂ = 2a", "geom-label-sm")

    # Auxiliary circle x^2 + y^2 = a^2 (locus of pedal feet Z1, Z2 — III.49)
    svg.circle(p_c, a, "geom-dashed", ref="( C A )")
    svg.ellipse_elem(p_c, a, b, "geom-bold")

    # Major axis and vertex tangents
    svg.seg((cx - a - 36, cy), (cx + a + 36, cy), "geom-line", ref="[ A1 A ]")
    svg.seg((cx - a, cy - 148), (cx - a, cy + 70), "geom-faint")
    svg.seg((cx + a, cy - 148), (cx + a, cy + 70), "geom-faint")

    # Tangent segment through Z1 - P - Z2 - K
    tdir = (p_z2[0] - p_z1[0], p_z2[1] - p_z1[1])
    svg.seg(
        (p_z1[0] - 0.22 * tdir[0], p_z1[1] - 0.22 * tdir[1]),
        (p_k[0] + 0.14 * tdir[0], p_k[1] + 0.14 * tdir[1]),
        "geom-accent-line",
        ref="[ Z1 Z2 ]",
    )

    # Focal radii PF1 and PF2
    svg.seg(p_f1, p_p, "geom-assert-line", ref="/ F1 P /")
    svg.seg(p_f2, p_p, "geom-assert-line", ref="/ F2 P /")

    # Perpendiculars F1 Z1 and F2 Z2 onto tangent
    svg.seg(p_f1, p_z1, "geom-hyper-line", ref="/ F1 Z1 /")
    svg.seg(p_f2, p_z2, "geom-hyper-line", ref="/ F2 Z2 /")
    svg.right_angle(p_z1, (p_p[0] - p_z1[0], p_p[1] - p_z1[1]), (p_f1[0] - p_z1[0], p_f1[1] - p_z1[1]), 8.5)
    svg.right_angle(p_z2, (p_p[0] - p_z2[0], p_p[1] - p_z2[1]), (p_f2[0] - p_z2[0], p_f2[1] - p_z2[1]), 8.5)

    # Equal tangent angles <F1 P Z1 = <F2 P Z2 (III.48 optical reflection!)
    svg.angle_arc(p_p, p_z1, p_f1, 22.0, "geom-rose-line")
    svg.angle_arc(p_p, p_f2, p_z2, 22.0, "geom-rose-line")

    svg.pt(p_ap, "A′", (-14, 15))
    svg.pt(p_a, "A", (12, 15))
    svg.pt(p_c, "C", (0, 17), lbl_cls="geom-label-sm")
    svg.pt(p_f1, "F₁", (-4, 18), "geom-point-assert", "geom-label-assert", ref="F1")
    svg.pt(p_f2, "F₂", (4, 18), "geom-point-assert", "geom-label-assert", ref="F2")
    svg.pt(p_p, "P", (4, -12), "geom-point-accent", "geom-label-accent")
    svg.pt(p_z1, "Z₁", (-14, -6), lbl_cls="geom-label-hyper", ref="Z1")
    svg.pt(p_z2, "Z₂", (13, -7), lbl_cls="geom-label-hyper", ref="Z2")
    svg.pt(p_k, "K", (12, -2), lbl_cls="geom-label-sm")
    svg.lbl((cx - 115, cy + 124), "Auxiliary Circle (r = a)", "geom-label-sm")
    svg.lbl((340, 344), "III.48: ∠F₁PZ₁ = ∠F₂PZ₂   ·   III.49: Z₁, Z₂ ∈ (C, a)   ·   III.52: PF₁ + PF₂ = AA′", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 7: Three-Line and Four-Line Locus — III.53–56 & Pappus/Descartes
# ---------------------------------------------------------------------------
def fig_three_four_line_locus() -> str:
    """Book III.53–56: Four-Line Locus d1·d3 = lambda d2·d4 on an inscribed quadrilateral."""
    svg = SvgCanvas("g7", "III.53-56", 680, 350)
    cx, cy = 340.0, 184.0
    a, b = 178.0, 108.0

    svg.lbl((340, 22), "III.53–56: The Three-Line & Four-Line Locus  (PQ₁ · PQ₃  =  λ · PQ₂ · PQ₄)", "geom-label-sm")
    svg.ellipse_elem((cx, cy), a, b, "geom-bold")

    def ep(deg: float) -> tuple[float, float]:
        rad = math.radians(deg)
        return (cx + a * math.cos(rad), cy - b * math.sin(rad))

    p_a = ep(148.0)
    p_b = ep(214.0)
    p_c = ep(332.0)
    p_d = ep(42.0)
    p_p = ep(94.0)  # Generic locus point P on the conic

    # Extend sides slightly to show the 4 fixed lines L1=AB, L2=BC, L3=CD, L4=DA
    lines_quad = [
        (p_a, p_b, "L₁", "geom-accent-line"),
        (p_b, p_c, "L₂", "geom-hyper-line"),
        (p_c, p_d, "L₃", "geom-accent-line"),
        (p_d, p_a, "L₄", "geom-hyper-line"),
    ]
    svg.poly([p_a, p_b, p_c, p_d], "geom-polygon", ref="< A B C D >")

    def foot_perp(pt: tuple[float, float], s1: tuple[float, float], s2: tuple[float, float]) -> tuple[float, float]:
        dx, dy = s2[0] - s1[0], s2[1] - s1[1]
        d2 = dx * dx + dy * dy
        t = ((pt[0] - s1[0]) * dx + (pt[1] - s1[1]) * dy) / d2
        return (s1[0] + t * dx, s1[1] + t * dy)

    for s1, s2, _lname, lcls in lines_quad:
        dx, dy = s2[0] - s1[0], s2[1] - s1[1]
        svg.seg((s1[0] - 0.16 * dx, s1[1] - 0.16 * dy), (s2[0] + 0.16 * dx, s2[1] + 0.16 * dy), lcls)

    q1 = foot_perp(p_p, p_a, p_b)
    q2 = foot_perp(p_p, p_b, p_c)
    q3 = foot_perp(p_p, p_c, p_d)
    q4 = foot_perp(p_p, p_d, p_a)

    # Opposite pair (Q1, Q3) in assert green vs (Q2, Q4) in rose
    svg.seg(p_p, q1, "geom-assert-line", ref="/ P Q1 /")
    svg.seg(p_p, q3, "geom-assert-line", ref="/ P Q3 /")
    svg.seg(p_p, q2, "geom-rose-line", ref="/ P Q2 /")
    svg.seg(p_p, q4, "geom-rose-line", ref="/ P Q4 /")

    for q_pt, s1, s2 in [(q1, p_a, p_b), (q2, p_b, p_c), (q3, p_c, p_d), (q4, p_d, p_a)]:
        svg.right_angle(q_pt, (s2[0] - s1[0], s2[1] - s1[1]), (p_p[0] - q_pt[0], p_p[1] - q_pt[1]), 7.5)

    svg.pt(p_a, "A", (-14, -6))
    svg.pt(p_b, "B", (-14, 14))
    svg.pt(p_c, "C", (14, 14))
    svg.pt(p_d, "D", (14, -6))
    svg.pt(p_p, "P", (0, -12), "geom-point-assert", "geom-label-assert")
    svg.pt(q1, "Q₁", (-15, 2), "geom-point-assert", "geom-label-assert", ref="Q1")
    svg.pt(q3, "Q₃", (15, 4), "geom-point-assert", "geom-label-assert", ref="Q3")
    svg.pt(q2, "Q₂", (-12, 14), "geom-point-rose", "geom-label-rose", ref="Q2")
    svg.pt(q4, "Q₄", (12, -8), "geom-point-rose", "geom-label-rose", ref="Q4")

    svg.lbl((148, 178), "L₁", "geom-label-accent")
    svg.lbl((316, 290), "L₂", "geom-label-hyper")
    svg.lbl((528, 198), "L₃", "geom-label-accent")
    svg.lbl((424, 96), "L₄", "geom-label-hyper")
    svg.lbl((340, 334), "Four-Line Locus: PQ₁·PQ₃ / (PQ₂·PQ₄) = const   (Three-Line when L₂ ≡ L₄: PQ₁·PQ₃ = λ·PQ₂²)", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 8: Conic Intersections & Four-Point Pencil — Book IV.25–57
# ---------------------------------------------------------------------------
def fig_four_point_conic_pencil() -> str:
    """Book IV.25–57: Two conics intersect in at most 4 points; bitangent conic counts as 2+2."""
    svg = SvgCanvas("g8", "IV.25-57", 740, 330)

    # Left panel: Transverse 4-point intersection of two symmetric ellipses
    # C1: x^2/a^2 + y^2/b^2 = 1, C2: x^2/b^2 + y^2/a^2 = 1 -> exact intersections (+/- s, +/- s)
    # where s = a*b / sqrt(a^2 + b^2)!
    c1x, c1y = 195.0, 178.0
    a1, b1 = 136.0, 74.0
    s_int = (a1 * b1) / math.sqrt(a1 * a1 + b1 * b1)

    svg.lbl((195, 22), "IV.25: At Most 4 Intersections", "geom-label-sm")
    svg.ellipse_elem((c1x, c1y), a1, b1, "geom-bold")
    svg.ellipse_elem((c1x, c1y), b1, a1, "geom-hyper-line")

    # Inscribed pencil quadrangle P1 P2 P3 P4
    pts4 = [
        (c1x - s_int, c1y - s_int, "P₁", (-15, -6), "P1"),
        (c1x + s_int, c1y - s_int, "P₂", (15, -6), "P2"),
        (c1x + s_int, c1y + s_int, "P₃", (15, 14), "P3"),
        (c1x - s_int, c1y + s_int, "P₄", (-15, 14), "P4"),
    ]
    svg.poly([(p[0], p[1]) for p in pts4], "geom-polygon-assert")
    svg.seg((pts4[0][0], pts4[0][1]), (pts4[2][0], pts4[2][1]), "geom-dashed")
    svg.seg((pts4[1][0], pts4[1][1]), (pts4[3][0], pts4[3][1]), "geom-dashed")
    for px, py, nm, off, rf in pts4:
        svg.pt((px, py), nm, off, "geom-point-assert", "geom-label-assert", ref=rf)
    svg.lbl((195, 316), "C₁ ∩ C₂ = {P₁, P₂, P₃, P₄}  (|C₁ ∩ C₂| ≤ 4)", "geom-label-sm")

    # Divider
    svg.seg((372, 20), (372, 316), "geom-faint")

    # Right panel: Double contact (IV.42–46) — two conics tangent at T1, T2 have ZERO further intersections!
    c2x, c2y = 556.0, 178.0
    a2, b2 = 142.0, 88.0
    b2_inner = 56.0
    svg.lbl((556, 22), "IV.42–46: Double Tangency Exhausts All 4", "geom-label-sm")
    svg.ellipse_elem((c2x, c2y), a2, b2, "geom-bold")
    svg.ellipse_elem((c2x, c2y), a2, b2_inner, "geom-accent-line")
    # Common tangents at T1(-a2, 0) and T2(+a2, 0)
    svg.seg((c2x - a2, c2y - 98), (c2x - a2, c2y + 98), "geom-rose-line", ref="[ T1 ]")
    svg.seg((c2x + a2, c2y - 98), (c2x + a2, c2y + 98), "geom-rose-line", ref="[ T2 ]")
    svg.seg((c2x - a2, c2y), (c2x + a2, c2y), "geom-dashed", ref="/ T1 T2 /")
    svg.pt((c2x - a2, c2y), "T₁ (mult. 2)", (-6, -104), "geom-point-rose", "geom-label-rose", ref="T1")
    svg.pt((c2x + a2, c2y), "T₂ (mult. 2)", (6, -104), "geom-point-rose", "geom-label-rose", ref="T2")
    svg.lbl((556, 316), "Bitangent Conics: 2 + 2 = 4 ⇒ Zero Further Common Points", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 9: Normals, Subnormals & the Astroidal Evolute — Book V.1–63
# ---------------------------------------------------------------------------
def _solve_ellipse_normals(a: float, b: float, x0: float, y0: float) -> list[float]:
    """Solve for all eccentric angles t in [0, 2pi) whose ellipse normal passes through (x0, y0)."""
    c2 = a * a - b * b

    def f_norm(t: float) -> float:
        return a * x0 * math.sin(t) - b * y0 * math.cos(t) - 0.5 * c2 * math.sin(2.0 * t)

    roots: list[float] = []
    n_grid = 2000
    for i in range(n_grid):
        t_lo = 2.0 * math.pi * i / n_grid
        t_hi = 2.0 * math.pi * (i + 1) / n_grid
        flo, fhi = f_norm(t_lo), f_norm(t_hi)
        if flo * fhi <= 0.0:
            lo, hi = t_lo, t_hi
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if f_norm(lo) * f_norm(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            r_val = 0.5 * (lo + hi)
            if not any(abs(r_val - prev) < 1e-4 for prev in roots):
                roots.append(r_val)
    return roots


def fig_normals_evolute() -> str:
    """Book V.1–63: Envelope evolute of normals to an ellipse & 4 normals from interior point O."""
    svg = SvgCanvas("g9", "V.1-63", 680, 380)
    cx, cy = 340.0, 194.0
    a, b = 196.0, 114.0
    c2 = a * a - b * b  # a^2 - b^2

    svg.lbl((340, 22), "V.51–62: Envelope of Normals (Astroidal Evolute) & Four Normals from Interior Point O", "geom-label-sm")
    svg.ellipse_elem((cx, cy), a, b, "geom-bold")
    svg.seg((cx - a - 22, cy), (cx + a + 22, cy), "geom-faint")
    svg.seg((cx, cy - b - 22), (cx, cy + b + 22), "geom-faint")

    # Family of subtle normals enveloping the evolute
    for k in range(36):
        th = 2.0 * math.pi * k / 36.0
        ex, ey = a * math.cos(th), b * math.sin(th)
        evx = (c2 / a) * (math.cos(th) ** 3)
        evy = -(c2 / b) * (math.sin(th) ** 3)
        svg.seg((cx + ex, cy - ey), (cx + evx, cy - evy), "geom-faint")

    # Exact astroidal evolute curve X = (c^2/a) cos^3 t, Y = -(c^2/b) sin^3 t
    ev_pts = [
        (cx + (c2 / a) * (math.cos(2 * math.pi * j / 240.0) ** 3),
         cy + (c2 / b) * (math.sin(2 * math.pi * j / 240.0) ** 3))
        for j in range(241)
    ]
    svg.curve(ev_pts, "geom-rose-line", closed=True, ref="( Evolute )")

    # Interior point O inside the evolute: solve f(t) = a*x0*sin t - b*y0*cos t - 0.5*c^2*sin(2t) = 0
    x0, y0 = 26.0, -18.0  # math coords (strictly inside evolute!)
    roots = _solve_ellipse_normals(a, b, x0, y0)
    assert len(roots) == 4, f"Expected 4 exact normal roots, got {len(roots)}"

    p_o = (cx + x0, cy - y0)
    lbl_offsets = [(10, -10), (-15, -10), (-15, 15), (12, 14)]
    for idx, rt in enumerate(roots, start=1):
        nx, ny = a * math.cos(rt), b * math.sin(rt)
        p_n = (cx + nx, cy - ny)
        # Tangent direction at N in SVG coords: (-a sin rt, -b cos rt)
        t_vec = (-a * math.sin(rt), -b * math.cos(rt))
        n_vec = (p_o[0] - p_n[0], p_o[1] - p_n[1])
        svg.seg(p_o, p_n, "geom-assert-line", ref=f"/ O N{idx} /")
        svg.right_angle(p_n, t_vec, n_vec, 7.5, "geom-assert-line")
        svg.pt(p_n, f"N_{idx}".translate(str.maketrans("1234", "₁₂₃₄")).replace("_", ""), lbl_offsets[idx - 1], "geom-point-assert", "geom-label-assert", ref=f"N{idx}")

    svg.pt(p_o, "O", (12, 5), "geom-point-accent", "geom-label-accent", ref="O", r=4.0)
    svg.lbl((cx + 96, cy - 42), "Evolute Envelope", "geom-label-rose")
    svg.lbl((340, 364), "Inside Evolute: 4 Normals (ON₁, ON₂, ON₃, ON₄)   ·   Outside Evolute: 2 Normals", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 10: Conjugate Diameters Parallelogram — VII.12 & VII.31
# ---------------------------------------------------------------------------
def fig_conjugate_diameters_theorems() -> str:
    """Book VII.12 & VII.31: Conjugate diameters CP=a', CD=b' with a'²+b'²=a²+b² & a'b'sin ω=ab."""
    svg = SvgCanvas("g10", "VII.12-31", 680, 360)
    cx, cy = 340.0, 188.0
    a, b = 158.0, 96.0

    # Principal axis rectangle (area 4ab)
    svg.poly(
        [(cx - a, cy - b), (cx + a, cy - b), (cx + a, cy + b), (cx - a, cy + b)],
        "geom-polygon",
    )
    svg.seg((cx - a, cy - b), (cx + a, cy - b), "geom-dashed")
    svg.seg((cx + a, cy - b), (cx + a, cy + b), "geom-dashed")
    svg.seg((cx + a, cy + b), (cx - a, cy + b), "geom-dashed")
    svg.seg((cx - a, cy + b), (cx - a, cy - b), "geom-dashed")

    # Conjugate semi-diameters at eccentric angle th and th + pi/2
    th = 0.58
    u = (a * math.cos(th), -b * math.sin(th))  # CP vector in SVG
    v = (-a * math.sin(th), -b * math.cos(th))  # CD vector in SVG

    p_c = (cx, cy)
    p_p = (cx + u[0], cy + u[1])
    p_pp = (cx - u[0], cy - u[1])
    p_d = (cx + v[0], cy + v[1])
    p_dp = (cx - v[0], cy - v[1])

    # Circumscribed conjugate tangent parallelogram K L M N = C +/- u +/- v
    k1 = (cx + u[0] + v[0], cy + u[1] + v[1])
    k2 = (cx - u[0] + v[0], cy - u[1] + v[1])
    k3 = (cx - u[0] - v[0], cy - u[1] - v[1])
    k4 = (cx + u[0] - v[0], cy + u[1] - v[1])

    svg.lbl((340, 22), "VII.12 & VII.31: Apollonius's Invariance Theorems on Conjugate Diameters", "geom-label-sm")
    svg.poly([k1, k2, k3, k4], "geom-polygon-accent", ref="< K L M N >")
    svg.seg(k1, k2, "geom-accent-line")
    svg.seg(k2, k3, "geom-accent-line")
    svg.seg(k3, k4, "geom-accent-line")
    svg.seg(k4, k1, "geom-accent-line")

    svg.ellipse_elem(p_c, a, b, "geom-bold")
    svg.seg((cx - a, cy), (cx + a, cy), "geom-faint", ref="/ A1 A /")
    svg.seg((cx, cy - b), (cx, cy + b), "geom-faint", ref="/ B1 B /")

    svg.seg(p_pp, p_p, "geom-assert-line", ref="/ P1 P /")
    svg.seg(p_dp, p_d, "geom-hyper-line", ref="/ D1 D /")
    svg.angle_arc(p_c, p_p, p_d, 26.0, "geom-rose-line", ref="< P C D )")

    svg.pt(p_c, "C", (-10, 15))
    svg.pt((cx + a, cy), "A", (12, 4), lbl_cls="geom-label-sm")
    svg.pt((cx, cy - b), "B", (10, -6), lbl_cls="geom-label-sm")
    svg.pt(p_p, "P", (12, -5), "geom-point-assert", "geom-label-assert")
    svg.pt(p_pp, "P′", (-14, 10), "geom-point-assert", "geom-label-assert")
    svg.pt(p_d, "D", (-12, -8), lbl_cls="geom-label-hyper")
    svg.pt(p_dp, "D′", (12, 12), lbl_cls="geom-label-hyper")
    svg.pt(k1, "K", (10, -8), "geom-point-accent", "geom-label-accent")
    svg.pt(k2, "L", (-12, -6), "geom-point-accent", "geom-label-accent")
    svg.pt(k3, "M", (-12, 12), "geom-point-accent", "geom-label-accent")
    svg.pt(k4, "N", (12, 10), "geom-point-accent", "geom-label-accent")

    svg.lbl((cx + 12, cy - 28), "ω", "geom-label-rose")
    svg.lbl((cx + 0.52 * u[0] + 6, cy + 0.52 * u[1] + 15), "a′", "geom-label-assert")
    svg.lbl((cx + 0.52 * v[0] - 12, cy + 0.52 * v[1] + 4), "b′", "geom-label-hyper")
    svg.lbl((340, 344), "VII.12: CP² + CD² = a′² + b′² = a² + b²   ·   VII.31: Area(KLMN) = 4 a′b′ sin ω = 4 ab", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 11: Problem of Apollonius (CCC — All 8 Tangent Circles)
# ---------------------------------------------------------------------------
def _solve_apollonius_ccc(
    c1: tuple[float, float, float],
    c2: tuple[float, float, float],
    c3: tuple[float, float, float],
) -> list[tuple[float, float, float, tuple[int, int, int]]]:
    """Solve exact quadratic algebraic system for all 8 circles tangent to C1, C2, C3."""
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    x3, y3, r3 = c3
    solutions: list[tuple[float, float, float, tuple[int, int, int]]] = []

    a11, a12 = 2.0 * (x2 - x1), 2.0 * (y2 - y1)
    a21, a22 = 2.0 * (x3 - x1), 2.0 * (y3 - y1)
    det = a11 * a22 - a12 * a21

    c1_sq = x1 * x1 + y1 * y1 - r1 * r1
    c2_sq = x2 * x2 + y2 * y2 - r2 * r2
    c3_sq = x3 * x3 + y3 * y3 - r3 * r3
    d10 = c2_sq - c1_sq
    d20 = c3_sq - c1_sq

    for s1 in (-1, 1):
        for s2 in (-1, 1):
            for s3 in (-1, 1):
                # 2(x_i - x_1)x + 2(y_i - y_1)y = d_i0 + 2(s_1 r_1 - s_i r_i) R
                e1 = 2.0 * (s1 * r1 - s2 * r2)
                e2 = 2.0 * (s1 * r1 - s3 * r3)
                # x = mx0 + mx1 * R, y = my0 + my1 * R
                mx0 = (d10 * a22 - a12 * d20) / det
                mx1 = (e1 * a22 - a12 * e2) / det
                my0 = (a11 * d20 - d10 * a21) / det
                my1 = (a11 * e2 - e1 * a21) / det

                # Substitute into (x - x1)^2 + (y - y1)^2 = (R - s1 r1)^2:
                # wait: if R + s1 r1 > 0, let's check (x - x1)^2 + (y - y1)^2 - (R + s1 r1)^2 = 0
                # Note: with (R + s_i r_i)^2 = R^2 + 2 s_i r_i R + r_i^2,
                # subtracting i=1 from i=2 gives 2(x2-x1)x + 2(y2-y1)y = d10 - 2(s2 r2 - s1 r1)R = d10 + e1 R!
                ux0, uy0 = mx0 - x1, my0 - y1
                qa = mx1 * mx1 + my1 * my1 - 1.0
                qb = 2.0 * (ux0 * mx1 + uy0 * my1 - s1 * r1)
                qc = ux0 * ux0 + uy0 * uy0 - r1 * r1
                disc = qb * qb - 4.0 * qa * qc
                if disc < 0.0:
                    continue
                sd = math.sqrt(disc)
                for root_r in ((-qb - sd) / (2.0 * qa), (-qb + sd) / (2.0 * qa)):
                    if root_r <= 1e-5:
                        continue
                    rx = mx0 + mx1 * root_r
                    ry = my0 + my1 * root_r
                    # Verify exact tangency to all three given circles:
                    # dist(center, c_i) == |root_r + s_i * r_i| and root_r + s_i * r_i >= 0
                    if root_r + s1 * r1 < -1e-5 or root_r + s2 * r2 < -1e-5 or root_r + s3 * r3 < -1e-5:
                        continue
                    ok = True
                    for xi, yi, ri, si in ((x1, y1, r1, s1), (x2, y2, r2, s2), (x3, y3, r3, s3)):
                        if abs(math.hypot(rx - xi, ry - yi) - abs(root_r + si * ri)) > 1e-5:
                            ok = False
                            break
                    if not ok:
                        continue
                    if not any(
                        math.hypot(rx - sx, ry - sy) < 1e-3 and abs(root_r - sr) < 1e-3
                        for sx, sy, sr, _ in solutions
                    ):
                        solutions.append((rx, ry, root_r, (s1, s2, s3)))
    return solutions


def fig_problem_of_apollonius_ccc() -> str:
    """Lost Tangencies (Pappus VII): All 8 exact Apollonius circles tangent to C1, C2, C3."""
    svg = SvgCanvas("g11", "Tangencies-CCC", 680, 420)
    ox, oy = 340.0, 214.0

    # Three asymmetric given circles chosen so all 8 tangent circles stay compact in viewBox!
    c1 = (-62.0, -34.0, 30.0)
    c2 = (66.0, -26.0, 24.0)
    c3 = (4.0, 62.0, 27.0)
    sols = _solve_apollonius_ccc(c1, c2, c3)
    assert len(sols) == 8, f"Expected 8 exact Apollonius CCC circles, got {len(sols)}"

    svg.lbl((340, 22), "Lost Tangencies (Pappus VII): The Problem of Apollonius (CCC — All 8 Tangent Circles)", "geom-label-sm")

    # Classify the 8 circles into Gergonne pairs for clear visual hierarchy
    for idx, (rx, ry, rr, signs) in enumerate(sorted(sols, key=lambda s: s[2]), start=1):
        if signs == (-1, -1, -1):
            cls = "geom-assert-line"  # Inner Soddy-type circle externally tangent to all 3
        elif signs == (1, 1, 1):
            cls = "geom-accent-line"  # Outer circumscribing circle internally tangent to all 3
        elif sum(signs) < 0:
            cls = "geom-hyper-line"
        else:
            cls = "geom-rose-line"
        svg.circle((ox + rx, oy + ry), rr, cls, ref=f"( S{idx} )")

    # Draw the three given circles boldly on top so tangencies stand out crisply
    for idx, (gx, gy, gr) in enumerate((c1, c2, c3), start=1):
        svg.poly(
            [
                (ox + gx + gr * math.cos(2 * math.pi * k / 48), oy + gy + gr * math.sin(2 * math.pi * k / 48))
                for k in range(48)
            ],
            "geom-polygon",
        )
        svg.circle((ox + gx, oy + gy), gr, "geom-bold", ref=f"( C{idx} )")
        svg.pt((ox + gx, oy + gy), f"C_{idx}".translate(str.maketrans("123", "₁₂₃")).replace("_", ""), (0, 5), ref=f"C{idx}")

    svg.lbl((340, 404), "Given C₁, C₂, C₃ (bold):  1 externally tangent (green) · 1 enclosing (gold) · 6 mixed-contact pairs (blue/rose)", "geom-label-sm")

    return svg.render()


# ---------------------------------------------------------------------------
# Plate 12: Apollonius Circle Locus (PA : PB = k) & Isodynamic Points X(15), X(16)
# ---------------------------------------------------------------------------
def fig_apollonius_circle_locus() -> str:
    """Lost Plane Loci II & ETC Bridge: PA:PB = k circle & Isodynamic Points X(15), X(16)."""
    svg = SvgCanvas("g12", "Plane-Loci-II-ETC", 760, 360)

    # Left panel: Single Apollonius Circle PA : PB = k = 5/3 on diameter I1 I2
    svg.lbl((190, 22), "Plane Loci II: Locus PA : PB = k", "geom-label-sm")
    ax, bx, y_ab = 64.0, 176.0, 206.0
    k_rat = 5.0 / 3.0
    # Internal I1: (ax + k*bx)/(1+k), External I2: (k*bx - ax)/(k - 1)
    x_i1 = (ax + k_rat * bx) / (1.0 + k_rat)
    x_i2 = (k_rat * bx - ax) / (k_rat - 1.0)
    cx_ap = 0.5 * (x_i1 + x_i2)
    r_ap = 0.5 * (x_i2 - x_i1)

    th_p = 2.08
    px_ap = cx_ap + r_ap * math.cos(th_p)
    py_ap = y_ab - r_ap * math.sin(th_p)

    svg.seg((36, y_ab), (358, y_ab), "geom-line", ref="[ A B ]")
    svg.circle((cx_ap, y_ab), r_ap, "geom-accent-line", ref="( M I1 )")
    svg.seg((ax, y_ab), (px_ap, py_ap), "geom-bold", ref="/ A P /")
    svg.seg((bx, y_ab), (px_ap, py_ap), "geom-bold", ref="/ B P /")
    # Internal & external angle bisectors PI1 perp PI2
    svg.seg((px_ap, py_ap), (x_i1, y_ab), "geom-assert-line", ref="/ P I1 /")
    svg.seg((px_ap, py_ap), (x_i2, y_ab), "geom-rose-line", ref="/ P I2 /")
    svg.right_angle(
        (px_ap, py_ap),
        (x_i1 - px_ap, y_ab - py_ap),
        (x_i2 - px_ap, y_ab - py_ap),
        8.5,
    )

    svg.pt((ax, y_ab), "A", (-4, 18))
    svg.pt((bx, y_ab), "B", (0, 18))
    svg.pt((x_i1, y_ab), "I₁", (-4, -10), "geom-point-assert", "geom-label-assert", ref="I1")
    svg.pt((x_i2, y_ab), "I₂", (10, 18), "geom-point-rose", "geom-label-rose", ref="I2")
    svg.pt((cx_ap, y_ab), "M", (0, 18), lbl_cls="geom-label-sm")
    svg.pt((px_ap, py_ap), "P", (-8, -11), "geom-point-accent", "geom-label-accent")
    svg.lbl((190, 338), "PA : PB = AI₁ : I₁B = AI₂ : BI₂ = k   (∠I₁PI₂ = 90°)", "geom-label-sm")

    # Divider
    svg.seg((384, 20), (384, 344), "geom-faint")

    # Right panel: Three Apollonius Circles of Triangle ABC concurring at X(15) & X(16)!
    svg.lbl((572, 22), "ETC Bridge: Three Apollonius Circles ⇒ X(15), X(16)", "geom-label-sm")
    # Choose scalene triangle ABC so all 3 Apollonius circles have finite moderate radii and stay inside [395, 750]x[38, 322]
    ta = (536.0, 118.0)
    tb = (472.0, 232.0)
    tc = (624.0, 222.0)
    la = math.hypot(tc[0] - tb[0], tc[1] - tb[1])
    lb = math.hypot(tc[0] - ta[0], tc[1] - ta[1])
    lc = math.hypot(tb[0] - ta[0], tb[1] - ta[1])

    def apollonius_circle_of_vertex(
        v_opp: tuple[float, float],
        v1: tuple[float, float],
        v2: tuple[float, float],
        ratio_v1_to_v2: float,
    ) -> tuple[tuple[float, float], float]:
        # Locus {P : |P - v1| / |P - v2| = k}, k != 1 (passes through v_opp!)
        k = ratio_v1_to_v2
        i1 = ((v1[0] + k * v2[0]) / (1.0 + k), (v1[1] + k * v2[1]) / (1.0 + k))
        i2 = ((v1[0] - k * v2[0]) / (1.0 - k), (v1[1] - k * v2[1]) / (1.0 - k))
        ctr = (0.5 * (i1[0] + i2[0]), 0.5 * (i1[1] + i2[1]))
        rad = 0.5 * math.hypot(i2[0] - i1[0], i2[1] - i1[1])
        assert abs(math.hypot(v_opp[0] - ctr[0], v_opp[1] - ctr[1]) - rad) < 1e-6
        return ctr, rad

    ca_ctr, ca_r = apollonius_circle_of_vertex(ta, tb, tc, lc / lb)
    cb_ctr, cb_r = apollonius_circle_of_vertex(tb, tc, ta, la / lc)
    cc_ctr, cc_r = apollonius_circle_of_vertex(tc, ta, tb, lb / la)

    # Exact intersections X(15) & X(16) of two coaxal Apollonius circles (and verified on third!)
    dx_c, dy_c = cb_ctr[0] - ca_ctr[0], cb_ctr[1] - ca_ctr[1]
    d_cc = math.hypot(dx_c, dy_c)
    u_cc = (ca_r * ca_r - cb_r * cb_r + d_cc * d_cc) / (2.0 * d_cc)
    h_cc = math.sqrt(max(0.0, ca_r * ca_r - u_cc * u_cc))
    mx_cc = ca_ctr[0] + (u_cc / d_cc) * dx_c
    my_cc = ca_ctr[1] + (u_cc / d_cc) * dy_c
    i_p1 = (mx_cc - (h_cc / d_cc) * dy_c, my_cc + (h_cc / d_cc) * dx_c)
    i_p2 = (mx_cc + (h_cc / d_cc) * dy_c, my_cc - (h_cc / d_cc) * dx_c)
    assert abs(math.hypot(i_p1[0] - cc_ctr[0], i_p1[1] - cc_ctr[1]) - cc_r) < 1e-5
    assert abs(math.hypot(i_p2[0] - cc_ctr[0], i_p2[1] - cc_ctr[1]) - cc_r) < 1e-5

    # Determine which is inside triangle ABC -> X(15) (1st Isodynamic Point), outside -> X(16)
    cent = ((ta[0] + tb[0] + tc[0]) / 3.0, (ta[1] + tb[1] + tc[1]) / 3.0)
    if math.hypot(i_p1[0] - cent[0], i_p1[1] - cent[1]) < math.hypot(i_p2[0] - cent[0], i_p2[1] - cent[1]):
        x15, x16 = i_p1, i_p2
    else:
        x15, x16 = i_p2, i_p1

    # Clip/draw arcs cleanly inside right panel [392, 752] x [34, 318]
    def draw_clipped_circle(ctr: tuple[float, float], rad: float, cls: str) -> None:
        seg_pts: list[tuple[float, float]] = []
        for j in range(361):
            ang = 2.0 * math.pi * j / 360.0
            px, py = ctr[0] + rad * math.cos(ang), ctr[1] + rad * math.sin(ang)
            if 394.0 <= px <= 750.0 and 36.0 <= py <= 318.0:
                seg_pts.append((px, py))
            else:
                if len(seg_pts) >= 2:
                    svg.curve(seg_pts, cls)
                seg_pts = []
        if len(seg_pts) >= 2:
            svg.curve(seg_pts, cls)

    draw_clipped_circle(ca_ctr, ca_r, "geom-accent-line")
    draw_clipped_circle(cb_ctr, cb_r, "geom-hyper-line")
    draw_clipped_circle(cc_ctr, cc_r, "geom-rose-line")

    svg.poly([ta, tb, tc], "geom-polygon", ref="< TA TB TC >")
    svg.seg(ta, tb, "geom-bold")
    svg.seg(tb, tc, "geom-bold")
    svg.seg(tc, ta, "geom-bold")
    svg.seg(x15, x16, "geom-dashed", ref="[ X15 X16 ]")

    svg.pt(ta, "A", (-6, -10))
    svg.pt(tb, "B", (-12, 12))
    svg.pt(tc, "C", (12, 10))
    svg.pt(x15, "X(15)", (22, 4), "geom-point-assert", "geom-label-assert", ref="X15", r=3.8)
    svg.pt(x16, "X(16)", (22, -4), "geom-point-assert", "geom-label-assert", ref="X16", r=3.8)
    svg.lbl((572, 338), "a·PA = b·PB = c·PC  at Isodynamic Points X(15), X(16)", "geom-label-sm")

    return svg.render()


FIGURE_BUILDERS = {
    "fig_oblique_cone_sections.svg": fig_oblique_cone_sections,
    "fig_application_of_areas.svg": fig_application_of_areas,
    "fig_tangent_harmonic_division.svg": fig_tangent_harmonic_division,
    "fig_hyperbola_asymptotes_secant.svg": fig_hyperbola_asymptotes_secant,
    "fig_harmonic_pole_polar.svg": fig_harmonic_pole_polar,
    "fig_central_conic_foci.svg": fig_central_conic_foci,
    "fig_three_four_line_locus.svg": fig_three_four_line_locus,
    "fig_four_point_conic_pencil.svg": fig_four_point_conic_pencil,
    "fig_normals_evolute.svg": fig_normals_evolute,
    "fig_conjugate_diameters_theorems.svg": fig_conjugate_diameters_theorems,
    "fig_problem_of_apollonius_ccc.svg": fig_problem_of_apollonius_ccc,
    "fig_apollonius_circle_locus.svg": fig_apollonius_circle_locus,
}


def build_all_figures(out_dir: Path | None = None) -> list[Path]:
    """Generate all 12 `.euclid-graphic` SVG figures into `docsrc/_static/figures/`."""
    target_dir = out_dir or (Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "figures")
    target_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for filename, builder in FIGURE_BUILDERS.items():
        svg_text = builder()
        out_path = target_dir / filename
        out_path.write_text(svg_text, encoding="utf-8")
        written.append(out_path)
    return written


def main() -> int:
    written = build_all_figures()
    for p in written:
        print(f"Generated {p.name} ({p.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

