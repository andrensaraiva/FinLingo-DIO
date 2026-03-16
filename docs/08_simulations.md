# 8. Financial Simulations

## Overview
FinLingo includes **5 simple financial simulators** that let users plug in numbers and see results in real time. Each simulation includes an educational takeaway to reinforce learning.

All simulators follow the same UX pattern:
```
[Input fields] → [Calculate button] → [Result panel] → [Educational message from Fino]
```

---

## Simulation 1: 💳 Installment Calculator

### Purpose
Show users the **true cost** of buying something in installments vs. paying upfront, including interest.

### Required User Inputs
| Field | Type | Example |
|---|---|---|
| Item price | Currency ($) | $1,200 |
| Number of installments | Integer (2–48) | 12 |
| Monthly interest rate | Percentage (%) | 1.5% |

### Expected Output
| Output | Value |
|---|---|
| Monthly payment | $109.56 |
| Total amount paid | $1,314.72 |
| Total interest paid | $114.72 |
| Interest as % of price | 9.56% |

### Formula
$$M = P \times \frac{r(1+r)^n}{(1+r)^n - 1}$$

Where: $M$ = monthly payment, $P$ = principal, $r$ = monthly interest rate, $n$ = number of installments.

### Educational Message
> 🦊 **Fino says:** "Splitting into 12 installments at 1.5%/month means you're paying $114.72 extra — that's almost 10% more than the original price! If you can, paying in fewer installments (or upfront) saves real money."

---

## Simulation 2: 🏦 Loan Simulator

### Purpose
Help users understand the **total cost of borrowing** and how different terms affect their payments.

### Required User Inputs
| Field | Type | Example |
|---|---|---|
| Loan amount | Currency ($) | $10,000 |
| Annual interest rate | Percentage (%) | 8% |
| Loan term | Months or years | 36 months |

### Expected Output
| Output | Value |
|---|---|
| Monthly payment | $313.36 |
| Total amount repaid | $11,281.00 |
| Total interest paid | $1,281.00 |
| Effective annual rate | 8.30% |

### Comparison Feature
Show a mini-table comparing 3 terms side by side:
| Term | Monthly Payment | Total Interest |
|---|---|---|
| 24 months | $452.27 | $854.48 |
| 36 months | $313.36 | $1,281.00 |
| 48 months | $244.13 | $1,718.24 |

### Educational Message
> 🦊 **Fino says:** "Notice how a longer term means lower monthly payments but MORE total interest? A 48-month loan costs you $863.76 more in interest than a 24-month one. Time is money — literally!"

---

## Simulation 3: 🎯 Savings Goal Calculator

### Purpose
Show users **how long it takes to reach a savings goal** based on monthly contributions, or how much they need to save monthly to reach a goal by a target date.

### Required User Inputs
| Field | Type | Example |
|---|---|---|
| Savings goal | Currency ($) | $5,000 |
| Monthly contribution | Currency ($) | $200 |
| Annual interest rate (savings account) | Percentage (%) | 4% |

### Expected Output
| Output | Value |
|---|---|
| Months to reach goal | 24 months |
| Total contributed | $4,800 |
| Interest earned | $200 |
| Interest as % of goal | 4.0% |

### Alternative Mode
"I want to save $5,000 in 12 months" → calculates required monthly contribution.

### Educational Message
> 🦊 **Fino says:** "By saving $200/month in an account with 4% annual interest, you'd reach your $5,000 goal in about 24 months — and earn $200 in interest along the way! Even small amounts add up over time. The hardest part is starting."

---

## Simulation 4: 🛡️ Emergency Fund Planner

### Purpose
Help users **calculate their ideal emergency fund size** and create a plan to build it.

### Required User Inputs
| Field | Type | Example |
|---|---|---|
| Monthly essential expenses | Currency ($) | $2,000 |
| Months of coverage desired | Integer (3–12) | 6 |
| Current savings | Currency ($) | $1,500 |
| Monthly amount you can save | Currency ($) | $300 |

### Expected Output
| Output | Value |
|---|---|
| Target emergency fund | $12,000 |
| Amount still needed | $10,500 |
| Months to reach target | 35 months |
| Percentage complete | 12.5% |

### Visual
A progress bar showing current savings vs. target, with milestone markers at 3 months and 6 months.

### Educational Message
> 🦊 **Fino says:** "Your target is $12,000 (6 months of expenses). You're 12.5% there — great start! At $300/month, you'll be fully covered in about 35 months. Pro tip: Start with a mini-goal of 1 month of expenses ($2,000) — you're almost there!"

---

## Simulation 5: 🛒 Purchase Comparison Tool

### Purpose
Help users **compare the true cost** of buying something NOW (with credit/installments) vs. saving up and buying later.

### Required User Inputs
| Field | Type | Example |
|---|---|---|
| Item price | Currency ($) | $800 |
| Installment interest rate (monthly) | Percentage (%) | 2% |
| Number of installments | Integer | 10 |
| Savings rate (monthly, if saving up) | Currency ($) | $100 |
| Savings account interest rate (annual) | Percentage (%) | 4% |

### Expected Output
| Scenario | Total Cost | Time |
|---|---|---|
| **Buy now (installments)** | $879.84 | 10 months |
| **Save and buy later** | $800.00 (+ $12.30 earned) | ~8 months |
| **Difference** | You save $92.14 by waiting | 2 months less |

### Educational Message
> 🦊 **Fino says:** "Buying on installments costs you $79.84 in interest. But if you save $100/month, you'd have enough in ~8 months AND earn a bit of interest! The trade-off? You wait longer, but you save money and avoid debt. This isn't always possible, but when it is — it's worth considering."

---

## Simulation Summary Table

| # | Simulator | Complexity | Key Learning |
|---|---|---|---|
| 1 | Installment Calculator | Simple | True cost of installments |
| 2 | Loan Simulator | Medium | Impact of loan terms on cost |
| 3 | Savings Goal Calculator | Simple | Power of consistent saving |
| 4 | Emergency Fund Planner | Simple | Planning for financial safety |
| 5 | Purchase Comparison | Medium | Borrowing vs. saving trade-offs |

## Implementation Notes
- All calculations use **standard financial formulas** — no external API needed
- Results are **purely educational** — always include the disclaimer: *"This simulation is for learning purposes only. Actual results depend on real-world conditions, fees, and terms."*
- Input validation: prevent negative numbers, unrealistic rates, and zero values
- All simulators should be **responsive** and work on both desktop and mobile layouts
