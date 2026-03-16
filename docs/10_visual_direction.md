# 10. Visual Direction

## Style Direction
**Modern Edu-Fintech** — the intersection of a friendly learning app (Duolingo, Khan Academy) and a clean fintech product (Nubank, Revolut). It should feel:
- Professional enough to be taken seriously
- Playful enough to feel inviting
- Clean enough to not overwhelm
- Colorful enough to feel alive

**Keywords:** Clean, Friendly, Modern, Trustworthy, Playful-but-Smart

---

## Color Palette

### Primary Colors
| Name | Hex | Usage |
|---|---|---|
| **Emerald** (Primary) | `#10B981` | Primary buttons, progress bars, success states |
| **Teal** (Secondary) | `#14B8A6` | Accents, links, secondary actions |
| **Deep Navy** | `#1E293B` | Text, headers, dark backgrounds |

### Supporting Colors
| Name | Hex | Usage |
|---|---|---|
| **Warm Amber** | `#F59E0B` | XP indicators, streak fire, warnings |
| **Soft Coral** | `#F87171` | Error states, incorrect answers |
| **Sky Blue** | `#38BDF8` | Info callouts, "Did You Know?" boxes |
| **Lavender** | `#A78BFA` | Badges, level indicators |

### Neutrals
| Name | Hex | Usage |
|---|---|---|
| **White** | `#FFFFFF` | Card backgrounds, main background |
| **Snow** | `#F8FAFC` | Page background |
| **Light Grey** | `#E2E8F0` | Borders, dividers, disabled states |
| **Medium Grey** | `#94A3B8` | Placeholder text, secondary text |
| **Dark Slate** | `#334155` | Body text |

### Dark Mode (Nice-to-have)
| Name | Hex | Usage |
|---|---|---|
| **Dark Base** | `#0F172A` | Background |
| **Dark Surface** | `#1E293B` | Cards |
| **Dark Border** | `#334155` | Borders |

---

## Typography

### Font Families
| Use | Font | Fallback |
|---|---|---|
| **Headings** | **Inter** (Bold/Semibold) | system-ui, sans-serif |
| **Body** | **Inter** (Regular/Medium) | system-ui, sans-serif |
| **Monospace** (numbers, code) | **JetBrains Mono** | monospace |

**Why Inter:** Free, highly legible, excellent at small sizes, widely used in modern web/fintech products.

### Type Scale
| Level | Size | Weight | Usage |
|---|---|---|---|
| H1 | 28px | Bold (700) | Screen titles |
| H2 | 22px | Semibold (600) | Section headers |
| H3 | 18px | Semibold (600) | Card titles |
| Body | 16px | Regular (400) | Lesson text, descriptions |
| Body Small | 14px | Regular (400) | Secondary info, disclaimers |
| Caption | 12px | Medium (500) | Labels, metadata |
| XP/Numbers | 20px | Bold (700) | XP counters, stats |

---

## Iconography Style

- **Style:** Outlined, with rounded joins — friendly and modern
- **Weight:** 2px stroke, consistent across all icons
- **Source recommendation:** [Lucide Icons](https://lucide.dev/) (free, MIT) or [Phosphor Icons](https://phosphoricons.com/)
- **Size:** 24×24px standard, 20×20px compact, 32×32px feature cards
- **Color:** Inherit from context (primary, neutral, or state color)

### Key Icons Needed
| Purpose | Icon |
|---|---|
| Home | House |
| Learn | Book Open |
| Chat | Message Circle |
| Simulator | Calculator |
| Progress | Bar Chart |
| Profile | User |
| XP | Star |
| Streak | Flame |
| Settings | Gear |
| Badge | Award |
| Lock | Lock |
| Check | Check Circle |
| Close | X |

---

## Card & Button Styles

### Cards
```css
.card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    border: 1px solid #E2E8F0;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

### Buttons
| Type | Style |
|---|---|
| **Primary** | Emerald bg, white text, rounded-full, shadow-sm, bold |
| **Secondary** | White bg, emerald border, emerald text, rounded-full |
| **Ghost** | Transparent bg, emerald text, no border, underline on hover |
| **Danger** | Coral bg, white text (used only for destructive actions) |
| **Disabled** | Light grey bg, medium grey text, no pointer events |

```css
.btn-primary {
    background: #10B981;
    color: #FFFFFF;
    border: none;
    border-radius: 9999px;
    padding: 12px 28px;
    font-weight: 600;
    font-size: 16px;
    box-shadow: 0 1px 3px rgba(16, 185, 129, 0.3);
    cursor: pointer;
    transition: background 0.15s ease;
}
.btn-primary:hover {
    background: #059669;
}
```

---

## Spacing and Layout

### Spacing Scale (based on 4px grid)
| Token | Value | Usage |
|---|---|---|
| `xs` | 4px | Tight gaps, icon-label spacing |
| `sm` | 8px | Inner card padding, list gaps |
| `md` | 16px | Section spacing, default padding |
| `lg` | 24px | Card padding, section gaps |
| `xl` | 32px | Major section separators |
| `2xl` | 48px | Screen padding top/bottom |

### Layout Principles
- **Max content width:** 480px (mobile-first) or 800px (desktop centered)
- **Side padding:** 16px minimum
- **Card gap:** 12px between stacked cards
- **Section gap:** 32px between sections
- **Bottom navigation:** Fixed, 64px height, 4–5 items

### Grid
- Single-column layout for most screens (mobile-first)
- 2-column grid for badge display and simulator cards

---

## Illustrations and Mascot

### Fino (Mascot) Illustrations
- **Style:** Flat 2D vector, limited to 3–4 colors from the palette
- **Expressions:** 5 core poses:
  1. 👋 Waving (welcome, greeting)
  2. 🎉 Celebrating (correct answer, badge unlock)
  3. 🤔 Thinking (loading, processing)
  4. 💪 Encouraging (wrong answer, retry)
  5. 📊 Presenting (simulation results, lessons)
- **Size:** 80–120px in context, 200px+ on splash/onboarding
- **Placement:** Inline with content, never blocking UI

### Spot Illustrations
Simple, icon-like illustrations for:
- Each learning track (credit card, piggy bank, shield, etc.)
- Onboarding screens
- Empty states ("No badges yet — start learning!")
- Celebration overlays

**Style:** Consistent with icon set — outline + flat fill, rounded, emerald/teal palette

### Illustration Resources (Free)
- [unDraw](https://undraw.co/) — customizable color, SVG
- [Open Doodles](https://www.opendoodles.com/) — casual illustrations
- [Humaaans](https://www.humaaans.com/) — modular people illustrations
- Custom Fino — can be created in Figma or as simple SVGs
