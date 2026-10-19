#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Scenario model for the break-even analysis in economic-model.md.

Every input below is either (a) an ASSUMPTION chosen by the author to span a
plausible range, or (b) a figure taken from a cited source (see the SOURCE
comments and evidence-register.md). Nothing here is an observed outcome.
The model answers one question only: how much analyst time per document would
the intervention have to save for its incremental cost to be recovered?
It does not forecast revenue, pricing, adoption or ROI.

Run: python3 economic_model.py
"""

from itertools import product

# ---- Inputs -----------------------------------------------------------------
PAGES_PER_DOC = {"low": 80, "base": 150, "high": 300}  # ASSUMPTION

# Parsing cost per page, USD.
BASELINE_PARSE_PER_PAGE = 0.0  # ASSUMPTION: open-source text extractor, compute cost ignored
# SOURCE E27: LlamaIndex pricing page lists $1.25 per 1,000 credits; credits/page by mode NOT
# stated on that page, so 1-10 credits/page is an ASSUMPTION.
CREDIT_USD = 1.25 / 1000
STRUCTURE_PARSE_PER_PAGE = {
    "open-source layout model (compute only)": 0.002,  # ASSUMPTION
    "commercial parser, 4 credits/page": 4 * CREDIT_USD,  # credits/page ASSUMPTION
    "VLM/LLM page parsing": 0.05,  # SOURCE E22 (approx. GPT-5.1 cost/page, unverified third-party figure)
}

QUESTIONS_PER_DOC = {"low": 10, "base": 25, "high": 50}  # ASSUMPTION
# Extra LLM/verification cost per question for the intervention (validation pass,
# larger context of table chunks). ASSUMPTION, USD.
BASELINE_LLM_PER_Q = 0.01
INTERVENTION_LLM_PER_Q = {"low": 0.02, "base": 0.04, "high": 0.10}

# Analyst fully-loaded cost per hour, USD. ASSUMPTION (not sourced).
ANALYST_RATE = {"low": 40, "base": 80, "high": 150}

# Fixed monthly cost to run and maintain the intervention (engineering share, security
# review, evaluation upkeep). ASSUMPTION, USD per month.
FIXED_MONTHLY = {"low": 10_000, "base": 40_000, "high": 120_000}

# ---- Calculations -----------------------------------------------------------

def incremental_variable_cost(pages, questions, parse_per_page, intervention_llm_q):
    parse = (parse_per_page - BASELINE_PARSE_PER_PAGE) * pages
    llm = (intervention_llm_q - BASELINE_LLM_PER_Q) * questions
    return parse + llm


def breakeven_minutes(cost_usd, rate_per_hour):
    """Analyst minutes per document that must be saved to offset cost_usd."""
    return cost_usd / rate_per_hour * 60


def main():
    print("Table A: incremental variable cost per document (USD)")
    print(f"{'parser':45s} {'pages':>6s} {'Qs':>4s} {'LLM/Q':>6s} {'cost':>8s}")
    rows = []
    for (pname, ppp), pages, qs, lq in product(
        STRUCTURE_PARSE_PER_PAGE.items(),
        [PAGES_PER_DOC["base"], PAGES_PER_DOC["high"]],
        [QUESTIONS_PER_DOC["base"]],
        [INTERVENTION_LLM_PER_Q["base"], INTERVENTION_LLM_PER_Q["high"]],
    ):
        c = incremental_variable_cost(pages, qs, ppp, lq)
        rows.append((pname, pages, qs, lq, c))
        print(f"{pname:45s} {pages:6d} {qs:4d} {lq:6.2f} {c:8.3f}")

    print("\nTable B: analyst minutes saved per document needed to recover variable cost")
    print(f"{'scenario (parser / pages / LLM per Q)':58s} " + " ".join(f"@${r}/h" for r in ANALYST_RATE.values()))
    for pname, pages, qs, lq, c in rows:
        label = f"{pname} / {pages}p / ${lq:.2f}"
        vals = " ".join(f"{breakeven_minutes(c, r):7.2f}" for r in ANALYST_RATE.values())
        print(f"{label:58s} {vals}")

    # Worst plausible variable-cost case vs best case
    lo = incremental_variable_cost(PAGES_PER_DOC["low"], QUESTIONS_PER_DOC["low"],
                                   STRUCTURE_PARSE_PER_PAGE["open-source layout model (compute only)"],
                                   INTERVENTION_LLM_PER_Q["low"])
    hi = incremental_variable_cost(PAGES_PER_DOC["high"], QUESTIONS_PER_DOC["high"],
                                   STRUCTURE_PARSE_PER_PAGE["VLM/LLM page parsing"],
                                   INTERVENTION_LLM_PER_Q["high"])
    print(f"\nBest-case incremental variable cost/doc:  ${lo:.3f}")
    print(f"Worst-case incremental variable cost/doc: ${hi:.3f}")

    print("\nTable C: documents per month needed so that analyst time saved covers the fixed monthly cost")
    print("(variable cost per doc = base case: commercial parser, 150 pages, 25 Qs, $0.04/Q;")
    print(" minutes saved per doc is the input being varied)")
    base_var = incremental_variable_cost(
        PAGES_PER_DOC["base"], QUESTIONS_PER_DOC["base"],
        STRUCTURE_PARSE_PER_PAGE["commercial parser, 4 credits/page"],
        INTERVENTION_LLM_PER_Q["base"])
    print(f"base variable cost/doc = ${base_var:.3f}")
    print(f"{'fixed/month':>12s} {'rate':>6s} " + " ".join(f"{m:>5d}min" for m in (5, 15, 30, 60)))
    for fname, F in FIXED_MONTHLY.items():
        for rname, rate in ANALYST_RATE.items():
            cells = []
            for m in (5, 15, 30, 60):
                net = m / 60 * rate - base_var
                cells.append(f"{F / net:8.0f}" if net > 0 else "     n/a")
            print(f"{F:12,d} {rate:6d} " + " ".join(cells))


if __name__ == "__main__":
    main()
