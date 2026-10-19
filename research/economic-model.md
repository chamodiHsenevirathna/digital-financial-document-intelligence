# Economic Model (scenario analysis, not a forecast)

**What this is:** a break-even style scenario model showing how much analyst time per document a verified pipeline would need to save to recover its incremental cost, under assumptions the author chose to span a plausible range.

**What this is not:** a revenue forecast, ROI estimate, market-size estimate, pricing recommendation, or evidence of demand. **The commercial case is unvalidated.** No credible willingness-to-pay data, customer commitments, or pricing for competing products was found (see §6). Observed financial outcomes: none. Everything below is a modeled scenario.

Reproduce all numbers with `python3 -I research/economic_model.py` (standard library only). Evidence IDs refer to [../evidence-register.md](../evidence-register.md).

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

## 3. Results (computed by the script)

Incremental variable cost = (parse cost/page − baseline parse cost) × pages + (intervention LLM/Q − baseline LLM/Q) × questions.

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

**Table B — analyst minutes saved per document needed to recover the variable cost**

| Scenario | @ $40/h | @ $80/h | @ $150/h |
|---|---:|---:|---:|
| Open-source layout / 150p / $0.04 | 1.58 | 0.79 | 0.42 |
| Open-source layout / 150p / $0.10 | 3.83 | 1.91 | 1.02 |
| Commercial / 150p / $0.04 | 2.25 | 1.12 | 0.60 |
| Commercial / 300p / $0.10 | 5.63 | 2.81 | 1.50 |
| VLM parsing / 150p / $0.04 | 12.38 | 6.19 | 3.30 |
| VLM parsing / 300p / $0.10 | 25.88 | 12.94 | 6.90 |

(Full table in the script output; selected rows shown.)

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
