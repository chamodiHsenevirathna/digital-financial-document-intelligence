# Research Plan

**Status:** Desk research completed 2026-10-19. No primary research (interviews, surveys, observation) and no experiments were run. Items marked *planned* are not done.

## 1. Research questions

| ID | Question | Answered by |
|---|---|---|
| RQ1 | Which of nine candidate failure categories (parsing, table structure, retrieval, calculation, hallucination, citations, missing/contradictory evidence, verification burden, security) are documented, plausible, or unevidenced? | [problem-discovery](research/problem-discovery.md), [evidence-register](evidence-register.md) |
| RQ2 | Which user segment has the clearest recurring problem, and what does the current workflow look like? | problem-discovery (desk research only; *interviews planned*) |
| RQ3 | What do existing products and open-source tools already do, and where is a gap actually demonstrated? | [competitive-landscape](research/competitive-landscape.md) |
| RQ4 | How much of end-to-end failure is attributable to parsing vs chunking vs retrieval vs reasoning vs verification? | [technical-analysis](research/technical-analysis.md), [evaluation-plan](research/evaluation-plan.md) |
| RQ5 | Which tasks belong in deterministic code, which in an LLM? | technical-analysis |
| RQ6 | What experiment would show whether a structure-aware, verified pipeline beats a plain PDF-to-text RAG baseline, and which component matters? | evaluation-plan |
| RQ7 | Is there a defensible commercial case, and what is missing to judge it? | [economic-model](research/economic-model.md) |

## 2. Hypothesis under test (not assumed true)

> H: Financial analysts may struggle to trust AI-generated financial analysis when PDF parsing loses table structure, retrieval misses relevant evidence, or LLMs perform calculations without reliable verification. A system combining structure-aware parsing, RAG, deterministic calculations and evidence verification may improve accuracy, traceability and analyst efficiency.

Sub-hypotheses, each falsifiable:
- **H1** Parsing/table-structure loss is a material cause of wrong answers (vs. retrieval or reasoning).
- **H2** Retrieval misses are a material cause of wrong answers.
- **H3** LLM-only arithmetic/column selection errors are material even with correct context.
- **H4** Deterministic computation plus validation reduces wrong answers without unacceptable abstention.
- **H5** Analysts spend meaningful time verifying AI output, and traceable evidence reduces that time.
- **H6** A gap exists that existing products do not already cover for a specific segment.

## 3. Search strategy

Searches were run via a web-search tool and direct page fetches on 2026-10-19. Query families:
1. Benchmarks: FinQA, TAT-QA, ConvFinQA, FinanceBench, DocFinQA, Fin-RATE.
2. Parsing/chunking: "PDF table extraction financial", Docling, Unstructured, LlamaParse benchmark.
3. RAG failure analysis: "failure points RAG", "financial report chunking".
4. Deterministic computation: Program of Thoughts, PAL.
5. Citation reliability and hallucination in RAG products (legal, search).
6. Security: OWASP prompt injection.
7. Market: Hebbia, Rogo, Daloopa, Claude for Financial Services, AlphaSense; analyst trust surveys.
8. Practitioner signals: Reddit and blog queries (Reddit returned nothing retrievable).
9. Data availability: SEC EDGAR structured data.

Papers were opened on arXiv. For two (E14 and E15) the PDF text was extracted locally and partly read; for most others only the abstract page was read. The depth of inspection for each is recorded in the evidence register.

## 4. Source hierarchy

1. Peer-reviewed papers and official dataset repositories/documentation.
2. Preprints with disclosed methods (flagged as unreviewed).
3. Official product/standards documentation (OWASP, SEC).
4. Vendor-authored benchmarks and pages: usable for *what is claimed*, never for comparative performance.
5. Secondary summaries, surveys without methodology, blogs, practitioner anecdotes: qualitative signals only.

## 5. Inclusion and exclusion criteria

Included: sources directly about financial document QA, PDF/table parsing, RAG components, numerical reasoning with tools, citation faithfulness, relevant security guidance, or the market landscape. Adjacent-domain sources (legal, web search) were included only as analogies and labeled `[INF]`.

Excluded: withdrawn papers (one found, listed in evidence register); sources with unverifiable statistics; claims appearing only in unsourced blog text. Sources known only from a search-result summary (code SNIP in the evidence register) were kept as low-confidence signals, are labeled as such, and are not treated as decisive evidence.

## 6. Evidence labeling

`[EST]` established, `[CON]` conflicting, `[INF]` inference, `[HYP]` hypothesis, `[GAP]` missing evidence. Confidence levels are defined in the evidence register.

## 7. Evaluation approach (summary)

An offline, reproducible comparison of a baseline PDF-to-text RAG and a structure-aware, deterministic, verified pipeline with component ablations, using public datasets plus independently verified questions on public filings. Details and acceptance criteria are in [research/evaluation-plan.md](research/evaluation-plan.md). **No experiment has been run.**

## 8. Decision rule

Recommendations must be proportionate to evidence. The decision options are: proceed to a limited prototype, conduct further problem validation, narrow the use case, change the solution, or do not pursue. The rule used: a prototype is justified only if (a) a specific user segment has a recurring, evidenced problem, (b) the failure sits in components the intervention addresses, and (c) the gap versus existing alternatives is demonstrated, not assumed. See the README for the outcome.

## 9. Limitations of this plan

- Desk research only; no user contact. Workflow descriptions are inferred from documents and vendor material.
- Fast-moving field: several relevant preprints are weeks to months old and not peer reviewed.
- Search tool coverage is incomplete (e.g., Reddit not retrievable). Absence of results is not evidence of absence.
- A single AI-assisted researcher with no independent reviewer. See [methodology](methodology/ai-use-and-research-limitations.md).
