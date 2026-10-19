# Economic Model (scenario analysis, not a forecast)

**What this is:** a break-even style scenario model showing how much analyst time per document a verified pipeline would need to save to recover its incremental cost, under assumptions the author chose to span a plausible range.

**What this is not:** a revenue forecast, ROI estimate, market-size estimate, pricing recommendation, or evidence of demand. **The commercial case is unvalidated.** No credible willingness-to-pay data, customer commitments, or pricing for competing products was found (see §6). Observed financial outcomes: none. Everything below is a modeled scenario.

Every figure below can be recomputed by hand or in a spreadsheet from the inputs in §1 and the formulas in §3; no code is needed. (The tables were first generated with a short Python script that has since been removed from the repository, because it contained no logic beyond the formulas stated here.) Evidence IDs refer to [../evidence-register.md](../evidence-register.md).

## 1. Inputs and their provenance

| Input | Values used | Provenance |
|---|---|---|
| Pages per document | 80 / 150 / 300 | **Assumption** |
| Questions per document | 10 / 25 / 50 | **Assumption** |
| Baseline parse cost | $0/page | **Assumption** (open-source extractor; compute ignored) |
| Open-source layout model parse cost | $0.002/page | **Assumption** (compute only) |
| Commercial parser cost | 4 credits/page × $1.25 per 1,000 credits = $0.005/page | Credit price from LlamaIndex pricing page (E27, accessed 2026-10-19); **4 credits/page is an assumption** because the page did not state per-mode credits |
| VLM/LLM page parsing | $0.05/page | E22 reports ≈$0.05/page for GPT-5.1 (approximate, unattributed third-party figure, low confidence) |
| Baseline LLM cost per question | $0.01 | **Assumption** |
| Intervention LLM cost per question | $0.02 / $0.04 / $0.10 | **Assumption** (extra verification pass and larger table context) |
| Analyst fully-loaded hourly cost | $40 / $80 / $150 | **Assumption**, not sourced |
| Fixed monthly cost (engineering share, security review, evaluation upkeep) | $10,000 / $40,000 / $120,000 | **Assumption** |

Not modeled (no evidence): integration and procurement effort, compliance certifications (e.g., SOC 2), sales cost, error-correction cost of residual wrong answers (see §5), insurance/liability, model price changes.

## 2. Cost categories (and the evidence status for each)

| Category | Driver | Status |
|---|---|---|
| Document processing | pages × parse cost | Partly sourced (E27, E22); mode credits unknown |
| Model/infrastructure | questions × LLM cost; hosting | Assumption |
| Human verification | minutes per document at analyst rate | Assumption; **no time-and-motion evidence** |
| Integration & maintenance | fixed monthly | Assumption |
| Security & compliance | fixed monthly | Assumption |
| Error correction & overhead | cost when a wrong answer is accepted | Not modeled; depends on the false acceptance rate, which is unmeasured |

## 3. Formulas and results

**Formulas** (all inputs from §1):

- **Incremental variable cost per document (V)** = (parse cost per page − baseline parse cost per page) × pages + (intervention LLM cost per question − baseline LLM cost per question) × questions. The baseline parse cost is $0 and the baseline LLM cost is $0.01 per question.
- **Break-even minutes per document (Table B)** = V ÷ analyst hourly rate × 60.
- **Documents per month to cover fixed cost (Table C)** = fixed monthly cost ÷ (minutes saved ÷ 60 × analyst hourly rate − V_base), where V_base = $1.50. Where the denominator is zero or negative, no volume breaks even ("n/a").
- **Worked example (Table A, row 5; Table B, row 5; Table C, row 2):** V = (0.005 − 0) × 150 + (0.04 − 0.01) × 25 = 0.75 + 0.75 = $1.50. At $80/h: 1.50 ÷ 80 × 60 = 1.125, shown as 1.13 minutes. For Table C at $10,000/month, $80/h and 5 minutes saved: 10,000 ÷ (5 ÷ 60 × 80 − 1.50) = 10,000 ÷ 5.1667 ≈ 1,935 documents.

**Table A — incremental variable cost per document (USD), 25 questions**

| Parser | Pages | LLM/Q | Cost |
|---|---:|---:|---:|
| Open-source layout (compute only) | 150 | $0.04 | 1.05 |
| Open-source layout | 150 | $0.10 | 2.55 |
| Open-source layout | 300 | $0.04 | 1.35 |
| Open-source layout | 300 | $0.10 | 2.85 |
| Commercial, 4 credits/page | 150 | $0.04 | 1.50 |
| Commercial, 4 credits/page | 150 | $0.10 | 3.00 |
| Commercial, 4 credits/page | 300 | $0.04 | 2.25 |
| Commercial, 4 credits/page | 300 | $0.10 | 3.75 |
| VLM/LLM page parsing | 150 | $0.04 | 8.25 |
| VLM/LLM page parsing | 150 | $0.10 | 9.75 |
| VLM/LLM page parsing | 300 | $0.04 | 15.75 |
| VLM/LLM page parsing | 300 | $0.10 | 17.25 |

Range across all inputs: **$0.26** (80 pages, 10 questions, open-source layout, $0.02/Q) to **$19.50** (300 pages, 50 questions, VLM parsing, $0.10/Q).

**Table B — analyst minutes saved per document needed to recover the variable cost** (all twelve scenarios of Table A, 25 questions). Values are rounded half-up to two decimals. Three cells that are exact halves (1.125, 14.625, 23.625) were shown as 1.12, 14.62 and 23.62 in an earlier version of this table because of floating-point formatting in the script that generated it; they are corrected here to match hand calculation. No conclusion changes.

| Scenario | @ $40/h | @ $80/h | @ $150/h |
|---|---:|---:|---:|
| Open-source layout / 150p / $0.04 | 1.58 | 0.79 | 0.42 |
| Open-source layout / 150p / $0.10 | 3.83 | 1.91 | 1.02 |
| Open-source layout / 300p / $0.04 | 2.03 | 1.01 | 0.54 |
| Open-source layout / 300p / $0.10 | 4.28 | 2.14 | 1.14 |
| Commercial / 150p / $0.04 | 2.25 | 1.13 | 0.60 |
| Commercial / 150p / $0.10 | 4.50 | 2.25 | 1.20 |
| Commercial / 300p / $0.04 | 3.38 | 1.69 | 0.90 |
| Commercial / 300p / $0.10 | 5.63 | 2.81 | 1.50 |
| VLM parsing / 150p / $0.04 | 12.38 | 6.19 | 3.30 |
| VLM parsing / 150p / $0.10 | 14.63 | 7.31 | 3.90 |
| VLM parsing / 300p / $0.04 | 23.63 | 11.81 | 6.30 |
| VLM parsing / 300p / $0.10 | 25.88 | 12.94 | 6.90 |

**Table C — documents per month needed for analyst time saved to cover fixed monthly cost.** Variable cost fixed at the base case ($1.50/doc: commercial parser, 150 pages, 25 questions, $0.04/Q). Cells = fixed cost ÷ (value of minutes saved − variable cost); "n/a" means the saved time is worth less than the variable cost.

| Fixed/month | Analyst $/h | 5 min saved | 15 min | 30 min | 60 min |
|---:|---:|---:|---:|---:|---:|
| 10,000 | 40 | 5,455 | 1,176 | 541 | 260 |
| 10,000 | 80 | 1,935 | 541 | 260 | 127 |
| 10,000 | 150 | 909 | 278 | 136 | 67 |
| 40,000 | 40 | 21,818 | 4,706 | 2,162 | 1,039 |
| 40,000 | 80 | 7,742 | 2,162 | 1,039 | 510 |
| 40,000 | 150 | 3,636 | 1,111 | 544 | 269 |
| 120,000 | 40 | 65,455 | 14,118 | 6,486 | 3,117 |
| 120,000 | 80 | 23,226 | 6,486 | 3,117 | 1,529 |
| 120,000 | 150 | 10,909 | 3,333 | 1,633 | 808 |

(The 5-minute, $40/h row is positive because 5 min × $40/h = $3.33 > $1.50.)

## 4. Sensitivity: what the arithmetic implies (conditional on the assumptions)

1. **Variable cost is small relative to analyst time unless VLM page-parsing is used on long documents.** With open-source or commercial parsers, recovering variable cost requires roughly 0.4–5.6 analyst-minutes saved per document across the rates above; with VLM parsing at 300 pages it requires up to ~26 minutes at $40/h.
2. **Fixed cost dominates the picture.** The monthly document volume needed to cover fixed cost ranges from under a hundred to tens of thousands (Table C). Whether a real customer segment has that volume is unknown.
3. **The decisive unknown is minutes saved per document**, which is the one input with no evidence. If the intervention saved nothing, no volume breaks even.
4. **Higher accuracy changes value through the cost of residual errors**, which this model omits. If a wrong accepted answer costs a firm materially (consequences of errors are a selection criterion), small reductions in false acceptance could dominate the savings from time. That requires measured false-acceptance rates, absent today.

## 5. Why no ROI figure is given

An ROI needs (a) time saved, (b) volume, (c) price or cost allocation, (d) error cost avoided. None of (a)–(d) is evidenced. Giving one would convert assumptions into apparent facts. The Datarails survey figure (26% of the week spent checking AI output, E21) is **not** used as an input: it is vendor-run, secondhand, reports no methodology, and concerns AI output in general rather than PDF analysis.

## 6. Missing commercial evidence (`[GAP]`)

- Willingness to pay, budgets, procurement cycles, and security-review hurdles for any segment.
- Pricing of competing products: Hebbia's page shows only "Request a demo"; Anthropic's page lists no price; Azure Document Intelligence prices did not load (placeholders). Press reports of competitor revenue and valuation (SNIP, E32) are unverified and say nothing about willingness to pay for this specific capability.
- Buyer identity: the analyst feels the problem, but the purchaser (team lead, innovation group, CIO, compliance) is unknown.
- Substitutes' real costs: data vendors, in-house scripts, offshore document preparation, free XBRL data (E25).
- Market size: **not estimated**; no credible source found, so none is given.

## 7. How to improve this model with evidence

Replace each assumption with a measured value: time-and-motion data from 5–10 analysts on a standard task (verification minutes with and without the tool); actual page/question counts from target workflows; quotes from vendors; measured false-acceptance and abstention rates from the [evaluation plan](evaluation-plan.md); and a loss estimate from reviewers for an accepted-wrong figure.
