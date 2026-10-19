# Beyond Chat with PDFs: Building Trustworthy AI for Financial Analysis

An evidence-based product-management case study. **Status: desk research complete (2026-10-19); no interviews, experiments or prototype.** This is a research investigation, not a product build, and the central hypothesis is tested rather than assumed.

> **Author and AI-use disclosure.** Repository owner: Chamodi Senevirathna, who supplied the research brief and the hypothesis under test. The research, analysis, writing and the economic-model script were produced by an AI model (Claude, via Claude Code) on 2026-10-19; source retrieval and summarization were AI-mediated. No interviews, surveys, product trials or experiments were conducted, and no human reviewer has independently verified the sources or calculations. [methodology/ai-use-and-research-limitations.md](methodology/ai-use-and-research-limitations.md) states what was and was not checked.

## Executive summary

- **Technical failures are real and documented on benchmarks:** retrieval misses, cross-period reasoning errors, and column/period mix-ups occur ([evidence E04, E15, E16](evidence-register.md)). Most numbers come from 2021–2024 models, so current error shares are unmeasured.
- **The hypothesis is only partly supported.** The one controlled parsing/chunking comparison found cheap parsers often competitive with complex ones (E14), free structured XBRL data exists for US public filers (E25), and several vendors already advertise source-linked answers (E32; claims unverified).
- **User and market evidence is weak.** No user research was done; the only demand signal is a vendor survey with no methodology (E21).
- **Recommendation: conduct further problem validation** on a narrowed use case (extracting and validating financial-statement figures from documents **without** structured filings), alongside an offline reliability experiment. **Do not build a product yet.**

## Problem statement

Analysts using AI on financial documents may not be able to trust results when parsing drops table structure, retrieval misses evidence, or an LLM does arithmetic without checks. Whether this is a *frequent, costly, un-served* problem for a specific user group is the open question.

## Research question and hypothesis

> Financial analysts may struggle to trust AI-generated financial analysis when PDF parsing loses table structure, retrieval misses relevant evidence, or LLMs perform calculations without reliable verification. A system combining structure-aware document parsing, RAG, deterministic calculations and evidence verification may improve accuracy, traceability and analyst efficiency.

Six falsifiable sub-hypotheses are defined in [research-plan.md](research-plan.md).

## Target users and workflow

Segments assessed: financial analysts, corporate finance, audit, research teams, compliance, plus credit/diligence analysts (added). The segment with the clearest PDF-specific problem is **provisionally** analysts working with financial documents lacking structured sources. This is an inference, not an observation. The workflow (collection → parsing → retrieval → analysis → calculation/verification → report → review) is mapped from desk research in [research/problem-discovery.md](research/problem-discovery.md), with explicit `[HYP]` labels where unobserved.

## Methodology

Desk research under a stated source hierarchy (peer-reviewed → preprint → official docs → vendor claims → anecdotes), an evidence register with inspection depth and confidence per source, and labels for established findings, conflicts, inferences, hypotheses, and gaps. Full detail: [research-plan.md](research-plan.md).

## Key findings

| Finding | Status | Evidence |
|---|---|---|
| Retrieval, cross-period and cross-entity analysis, and table-column mistakes degrade LLM performance on financial tasks | Documented on benchmarks (older models for some) | E04, E15, E16 |
| Offloading computation to code improved 2022-era model accuracy | Established for those models; margin today unknown | E07, E08 |
| Citations in RAG products can fail to support claims | Established in legal and web-search RAG; **not measured for finance** | E09, E10 |
| Lightweight PDF parsers were often competitive with more complex ones | Conflicts with "parsing is the main lever" (no table-structure-recognition parser such as Docling in the compared set) | E14 |
| Table-aware, metadata-aware pipelines report high FinanceBench accuracy (89.3%) | Self-reported preprint; component attribution not verified | E17 |
| Free structured XBRL data exists for US public filers | Official source | E25 |
| Several vendors market source-linked financial answers | Vendor claims, unverified | E32 |
| Analysts spend significant time verifying AI output | **Weak** (vendor survey, no methodology) | E21 |
| Willingness to pay | **No evidence** | [economic-model](research/economic-model.md) |

## Proposed product opportunity (provisional)

A verification-first extraction and period-comparison tool for financial-statement documents without structured filings: structure-aware parsing with explicit units/periods, deterministic calculation, rule-based validation, span-level provenance and abstention. Use-case scoring and the rationale for choosing this over cross-document reconciliation or open-ended Q&A are in [research/product-strategy.md](research/product-strategy.md). The scores are author judgments. Differentiation from incumbents is **a hypothesis**: citations, table-aware chunking and calculator use are not differentiators. Landscape: [research/competitive-landscape.md](research/competitive-landscape.md).

## Evaluation design

Baseline arms (plain PDF-to-text RAG; stronger hybrid baseline; frontier long-context model) versus an intervention arm (structure-aware parsing, table-aware retrieval, code-based calculation, rule/span verification, abstention), on the same documents and questions, with eight ablations including oracle-parse and oracle-retrieval conditions that localize loss. Metrics span extraction accuracy, retrieval, numerical accuracy, citation support, unsupported-answer rate, correct abstention, false acceptance, time, latency and cost. Datasets considered: FinQA, TAT-QA, ConvFinQA, FinanceBench, DocFinQA, Fin-RATE and a to-be-built verified set. **Nothing has been run; all expected outcomes are hypotheses.** See [research/evaluation-plan.md](research/evaluation-plan.md).

## Economic and operational considerations

A scenario model (reproducible with [research/economic_model.py](research/economic_model.py)) shows incremental variable cost per document of about **$0.26–$19.50** under author-chosen assumptions, and that break-even depends mainly on minutes of analyst time saved per document, the one input with no evidence. It includes **no revenue forecast, ROI or market size**, since credible data are unavailable. Security, privacy and financial correctness are treated as core requirements (prompt-injection exposure from uploaded files, access isolation, audit logging, no consequential actions) in [research/technical-analysis.md](research/technical-analysis.md). The commercial case is **unvalidated**. See [research/economic-model.md](research/economic-model.md).

## Final recommendation

**Conduct further problem validation.** Specifically:
1. Interview 8–12 analysts handling documents without structured filings (not yet done).
2. Run the offline reliability experiment as research, to learn which pipeline stage drives errors.
3. Revisit the build decision against pre-stated criteria: beat the best baseline by a set margin with low false acceptance, and confirmed buyer interest.

**Strongest counterarguments:** frontier long-context models may already suffice; verification effort may be policy-driven; incumbents may already serve the need; the niche may be too small. **Evidence that would change the decision** is listed in [research/product-strategy.md](research/product-strategy.md).

## Evidence limitations

Desk research only; most papers read at abstract level; vendor and secondary sources of low reliability; benchmarks dominated by 2021–2024 models; several key sources are 2026 preprints not peer reviewed; Reddit and forum evidence not retrievable; no competitor trial; no primary research. These limits mean this study **cannot establish** user demand, current commercial-tool accuracy, the share of errors by stage, any efficiency gain, or willingness to pay.

## Files

| File | Contents |
|---|---|
| [research-plan.md](research-plan.md) | Questions, search strategy, source hierarchy, inclusion criteria, decision rule |
| [evidence-register.md](evidence-register.md) | 28 register entries (some cover several sources) with URLs, dates, findings, limits, confidence, inspection depth |
| [research/problem-discovery.md](research/problem-discovery.md) | Failure categories, competing explanations, segments, workflow, evidence for/against |
| [research/competitive-landscape.md](research/competitive-landscape.md) | Existing tools and claimed capabilities, with verification status |
| [research/technical-analysis.md](research/technical-analysis.md) | Pipeline failure propagation, deterministic tooling, safe-design controls |
| [research/evaluation-plan.md](research/evaluation-plan.md) | Datasets, arms, ablations, metrics, acceptance criteria |
| [research/product-strategy.md](research/product-strategy.md) | Use-case scoring, product hypothesis, decision |
| [research/economic-model.md](research/economic-model.md) | Scenario model and missing commercial evidence |
| [research/economic_model.py](research/economic_model.py) | Script that regenerates the model's tables |
| [methodology/ai-use-and-research-limitations.md](methodology/ai-use-and-research-limitations.md) | AI disclosure, verification status, limitations |
| [LICENSE-CC-BY-4.0.txt](LICENSE-CC-BY-4.0.txt), [LICENSE-MIT.txt](LICENSE-MIT.txt) | License texts (see Licensing) |

## Reproducing the economic tables

```bash
python3 -I research/economic_model.py
```

## Licensing

| Material | License |
|---|---|
| Documentation and written case-study content: `README.md`, `research-plan.md`, `evidence-register.md`, everything in `research/` except the script, and everything in `methodology/` | [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CC-BY-4.0.txt) |
| Code: `research/economic_model.py` | [MIT](LICENSE-MIT.txt) |

Third-party sources cited here (papers, datasets, vendor pages) remain under their own terms; this repository links to them and quotes only short excerpts. Dataset licenses mentioned in the evidence register are as stated on the sources' pages and are not legal advice. The repository contains no credentials, personal data or confidential documents.
