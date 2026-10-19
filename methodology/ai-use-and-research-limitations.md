# AI Use and Research Limitations

This case study was produced with substantial AI assistance. This document states what the AI did, what a human checked, and what remains unverified. It is written to neither exaggerate nor minimize the AI's role.

## 1. How AI was used

| Activity | AI tool | Role |
|---|---|---|
| Research planning, structure, question framing | Claude (Anthropic) via the Claude Code CLI, session of 2026-10-19 | Drafted the plan and file structure from a task brief supplied by the repository owner |
| Source discovery | Claude using a web-search tool and a page-fetch tool | Ran searches, fetched pages and PDFs, and summarized them. The fetch tool answers questions about a page using a smaller model, so **summaries are AI-mediated, not verbatim reads** |
| Reading papers | Claude; for two papers (E14, E15) the PDF text was extracted locally with `pdftotext` and partly read by Claude | Extracted findings; most other papers were read at abstract-page level only |
| Analysis and synthesis | Claude | Categorized failure modes, drafted the comparison tables, scored use cases, wrote the evaluation plan |
| Calculations | Claude | Computed the economic tables with a short Python script during drafting. The script was later removed from the repository because it added nothing beyond the formulas now documented in `research/economic-model.md` |
| Writing | Claude drafted all text in this repository | |
| Coding | None in the published repository | |

**Human role.** The repository owner supplied the brief and hypothesis and is responsible for publication. At the time this document was written, the AI has no record that the owner independently verified any claim, source or calculation. That should be treated as not yet done unless the owner states otherwise in a revision.

## 2. What was and was not independently checked

**Sources directly opened by the AI (page content retrieved):** every URL listed in the evidence register with depth code ABS, GH, WEB or FULL. The depth code states how much was read.

**Sources not opened (search-result summary only, depth SNIP):** DocFinQA initial details (later opened as ABS), Procycons blog, FinanceBench long-context figures (the 76–79% and 25%→78% numbers come from search-result text quoting the paper), Hebbia vs Rogo comparison pages, Rogo funding reports, Daloopa partner pages, Claude-for-Excel secondary pages, CFO Impulse Substack, Capterra snippet. These are flagged Low confidence and are not used as decisive evidence.

**Quantitative claims independently re-checked by a second source or by calculation:**
- Table A–C arithmetic in the economic model: recomputed during a later review from the inputs and formulas written in `economic-model.md` alone, using a separately written calculation (all 12 Table A rows, all 12 Table B rows, all 9 Table C rows, the $0.26–$19.50 range and the break-even ranges quoted in §4), with no discrepancy found. This was done by the same AI, not by a human reviewer, and the inputs themselves are assumptions.
- Use-case weighted scores: computed by a separate short script (weights sum to 100).
- Everything else is **single-source**: figures such as FinanceBench's 81%, Fin-RATE's 18.60%/14.35% drops, TAT-QA's 58.0/90.8 F1 and the legal-RAG 17–33% come from the cited abstracts or pages and were not reproduced.

**Not checked:** accuracy of any vendor claim; dataset license details beyond what repo pages stated; whether cited arXiv abstracts match the final published versions; whether some 2026 preprints have been revised or withdrawn since access. One withdrawn paper was found and excluded (listed in the evidence register). Others may exist undetected.

**Known AI-process errors during this work (disclosed):**
- The AI initially guessed a wrong arXiv ID for DocFinQA (it was UltraTool). This was caught because the fetched page showed a different title, and the correct ID was found by search. This shows the risk of unverified identifiers; every arXiv identifier in the register was opened through a fetched page, and the title returned was matched to the cited title.
- A fetch tool reported that a pricing page showed placeholders instead of numbers; no price was invented.

## 3. Primary research actually conducted

| Activity | Done? |
|---|---|
| User interviews | **No** |
| Surveys | **No** |
| Workflow observation | **No** |
| Prototype or software experiments on parsers/RAG | **No** |
| Benchmark runs | **No** |
| Competitor product trials or demos | **No** |
| Pricing quotes | **No** |

Consequently the "Workflow" descriptions are inferences, and no user quotes appear anywhere. No statement in this repository reports that AI use was or was not disclosed to any participant, because no participants exist. If interviews or a user study are later conducted, AI use in the research must be disclosed to participants at that time, and this document updated.

## 4. Claims that remain unverified

- That the identified user segment (non-XBRL financial-statement documents) exists at meaningful scale.
- That parsing is a material contributor to wrong answers in current systems.
- Capability claims for Hebbia, Rogo, AlphaSense, Daloopa, Anthropic's financial offering, Docling and commercial parsers.
- The 89.3% FinanceBench figure (MimirRAG, self-reported; baseline and ablation not read).
- All use-case scores, weights and acceptance thresholds (author judgments).
- All economic-model inputs other than the LlamaIndex credit price.

## 5. Methodological limitations and biases

1. **Desk research only.** No demand-side evidence; the problem's existence for real users is inferred.
2. **Abstract-level reading** for most papers; details, caveats, and ablations may contradict the abstract.
3. **Search tool bias and gaps.** Results were from a US-only web-search tool and favored recent arXiv and vendor pages; Reddit and similar forums returned nothing. Absence of results is not evidence of absence.
4. **Recency and instability.** Many relevant sources are 2026 preprints without peer review; benchmarks use mostly 2021–2024 models, so findings may overstate present-day error rates.
5. **Vendor and secondary-source bias.** Vendor benchmarks and marketing were treated as claims, not performance; still, their selection into the review may skew the competitive picture.
6. **Confirmation risk.** The hypothesis was supplied up front; the AI may have been inclined to find supporting evidence. Mitigations: an explicit "against" section, a contested-evidence table, and a recommendation that does not endorse building.
7. **AI hallucination and summarization risk.** Page summaries came from a model; numbers were cross-referenced against text where possible but not always.
8. **Single reviewer, no external peer review.**
9. **Scoring subjectivity.** Use-case weights and scores are judgments; a different weighting could change the ranking.
10. **Model-generation drift.** Evidence and recommendations depend on the state of LLMs as of October 2026.

## 6. What a reviewer should do before relying on this

Open the cited URLs for any number that matters; read the full papers behind E04, E14, E15 and E17; recompute the economic tables with your own assumptions using the formulas in `research/economic-model.md`; and treat all `[HYP]` and `[GAP]` items as open questions.
