# Problem Discovery

Evidence IDs (E##) refer to [../evidence-register.md](../evidence-register.md). Labels: `[EST]` established, `[CON]` conflicting, `[INF]` inference, `[HYP]` hypothesis, `[GAP]` missing.

**Scope note.** This is desk research. No analyst, auditor or finance team was interviewed, surveyed or observed. Workflow descriptions below are my inference from benchmark designs, product pages and general domain knowledge, not observed practice.

## 1. Failure categories: what is documented?

| # | Category | Status | Strongest evidence | Main caveat |
|---|---|---|---|---|
| 1 | PDF parsing/extraction errors | `[EST]` that PDFs are hard to parse; `[HYP]` that it is the *dominant* cause of wrong answers | E14 (parsing and retrieval choices "strongly affect performance"), E13 (56% → 61.3%/76% with pre-processing) | E14 also finds lightweight parsers often match complex ones `[CON]`; E13 abstract does not attribute gains to a component |
| 2 | Loss of table structure, headers, units, periods, footnotes | `[INF]`, partially supported | E16 (models pull "data from incorrect adjacent columns"), E06 (element-based chunking helps), E17 (table-aware chunking credited) | Evidence is mostly abstract-level; units/footnote loss specifically is `[HYP]`: no study I read measured it directly |
| 3 | Retrieval failures in RAG | `[EST]` | E04 (GPT-4-Turbo with retrieval: 81% wrong or refused), E05, E15 (retrieval-augmented settings degrade) | E04 is 2023; E17 reports 89.3% on the same benchmark with a different pipeline `[CON]` (self-reported) |
| 4 | Incorrect numerical reasoning/calculation | `[EST]` for 2021–22 models; `[GAP]` for 2026 models | E01, E02 (large gap to experts), E07/E08 (interpreter offloading helps), E16 (collapse without formula hints) | Modern models are better at arithmetic; the *remaining* error share is unmeasured. E19 says numerical reasoning "varies widely by context" |
| 5 | Unsupported claims/hallucinations | `[EST]` in adjacent domains and for finance benchmarks | E04 (17–21% hallucination in long-context setups, SNIP), E09 (17–33% legal RAG), E15 (comparison hallucinations) | Rates depend on definitions and model generation |
| 6 | Incorrect/misleading citations | `[EST]` in generative search; `[INF]` for finance | E10 (51.5% sentence support, 74.5% citation precision) | Not measured for financial products. Vendors advertise source links (E32) but I found no independent test |
| 7 | Failure to detect missing/ambiguous/contradictory evidence | `[INF]` | E15 (temporal and entity mismatches), E04 (models refuse or answer wrongly) | No study I read measured abstention quality in finance. `[GAP]` |
| 8 | Excessive manual verification | `[HYP]` supported only by weak sources | E21 (vendor survey: 26% of week; n=270 CFOs, no methodology), E19 (friction "may shift" to evaluating outputs) | No time-and-motion data. The survey is about AI output generally, not PDF analysis |
| 9 | Security, confidentiality, auditability | `[EST]` as a general LLM risk (E26); `[GAP]` for finance-specific incident data | OWASP guidance on indirect injection from files | Not tested against any financial document assistant |

**Takeaway.** The technical failures (3, 4, 5) are the best documented, mostly on benchmarks with 2021–2024 models. Parsing and table-structure loss (1, 2) are plausible and partly supported, but the one controlled comparison of cheap parsers I read (E14) found small differences, so their share of end-to-end error is unknown. User-facing consequences (8) rest on weak evidence.

## 2. Competing explanations

| Observed symptom (analyst distrusts output) | Alternative explanation | Implication |
|---|---|---|
| Wrong number in answer | Question ambiguity (which period, GAAP vs adjusted, restated vs original) rather than extraction error | Better parsing would not help; need clarifying questions and period/basis metadata |
| Wrong number in answer | Right document not in the corpus or wrong filing version | Retrieval/corpus management, not parsing |
| Wrong calculation | Wrong inputs selected (adjacent column, wrong year) rather than wrong arithmetic | Calculator alone does not fix it; E16 points this way |
| Low trust | Lack of visible provenance, not low accuracy | A citation UI might raise trust even if accuracy is unchanged. Trust ≠ correctness `[INF]` |
| Extraction errors | PDF is the wrong input; structured XBRL is available for US filers (E25) | Use structured data when it exists; PDF parsing matters for the rest |
| High verification effort | Review is mandated by policy regardless of accuracy | Efficiency gains may be capped by compliance rules `[HYP]` |

## 3. Users and segments

Evidence on any segment's actual practice is thin, so the ranking below is an inference scored on *how clearly the problem follows from documented failure modes and workflow structure*. It is not measured demand.

| Segment | Recurring document-heavy task | Why it may feel the problem | Why it may not | Assessment |
|---|---|---|---|---|
| Buy-side/sell-side financial analysts | Extract, compare and model figures from filings, supplements, decks | Cross-period work degrades most (E15) | US-listed data available via XBRL and data vendors (E25, E32); well-funded incumbents | Clear tasks, crowded for public-company filings |
| Corporate finance/FP&A | Consolidating internal and counterparty documents | Errors affect reporting | Mostly internal structured systems (ERP) rather than PDFs `[HYP]` | Unclear PDF dependence |
| Audit professionals | Tie figures across documents to supporting evidence; sampling | Traceability is the core activity; errors have consequences | Strict confidentiality, tool-approval, methodology rules | High need for traceability; slow procurement `[HYP]` |
| Credit/diligence/lending teams, private-company analysis (not in the original list) | Spreading financials from PDFs without XBRL; reconciling across documents | No structured source for private or non-XBRL documents | Not investigated in depth | Plausible strongest PDF-specific gap `[HYP]`; added by me, needs validation |
| Compliance/reporting | Checking disclosures against rules | Rule-based checks fit deterministic tools | Regulated, narrow, mostly structured filings | Unclear |
| Financial research teams | Cross-company comparisons | Fin-RATE cross-entity drop 14.35% (E15) | Data vendors already sell normalized fundamentals (E32 Daloopa) | Crowded |

**Segment with the clearest recurring problem (provisional):** analysts who must extract and cross-check figures from **documents lacking structured filings** (e.g., private-company statements, non-US reports without equivalent tagging, supplemental decks, credit/diligence packages). This is an inference from E25 (structured data exists for US public filers) and E15/E16 (cross-period and table-column failures). It was not validated with any user. `[HYP]`

## 4. Workflow map (inferred, not observed)

| Stage | Goal | Common tools (general knowledge; not verified here) | Likely error/delay points | Detection and correction | Consequence | Who feels it / who pays |
|---|---|---|---|---|---|---|
| 1 Document collection | Gather the right versions | EDGAR, data rooms, email, vendor portals | Wrong version, restated figures, missing docs | Manual cross-checks | Analysis on wrong basis | Analyst; team lead owns budget `[HYP]` |
| 2 Parsing | Turn PDFs into usable text/tables | Copy-paste, PDF converters, OCR, vendor data | Merged cells, multi-line headers, scanned pages, footnotes | Visual inspection against PDF | Silent misalignment | Analyst |
| 3 Retrieval | Find the relevant passages/tables | Ctrl-F, search, RAG assistants | Misses relevant table or picks another year | Spot-checking; reading around | Missed evidence | Analyst |
| 4 Analysis | Interpret figures and context | Excel, Python, BI, assistants | Misreading adjustments, basis, scope | Peer review | Wrong conclusions | Analyst/PM |
| 5 Calculation & verification | Compute ratios; tie-outs | Excel, scripts | Wrong inputs, hard-coded values | Reconciliation, sub-total checks | Material errors if undetected | Reviewer/auditor |
| 6 Report preparation | Produce memo/model | Word, PowerPoint, Excel | Transcription errors | Review | Embarrassment, restatement | Team |
| 7 Human review | Approve | Manager/compliance | Review depth limited by time | Sampling | Residual risk accepted | Firm |

Purchasing: `[GAP]` I found no evidence on who owns the budget, security review timelines, or what teams currently spend.

## 5. Evidence for and against the hypothesis

**For**
- Retrieval, cross-period reasoning and table-column errors are documented on public benchmarks (E04, E15, E16).
- Offloading arithmetic to code improved accuracy for 2022-era models (E07, E08).
- A combined table-aware, metadata-aware, agentic pipeline reports 89.3% on FinanceBench (E17, self-reported), far above the 2023 baseline (E04).
- Citations frequently fail to support claims in adjacent systems (E09, E10), so verifiable evidence is a legitimate requirement.
- Output assessment is flagged as an emerging bottleneck (E19, `[INF]`).

**Against / complicating**
- Parser choice produced modest differences in the one controlled study, and lightweight parsers were often competitive (E14).
- Structured XBRL data exists for US public filers at no cost (E25), which weakens the PDF-centric premise for that segment.
- Several well-funded incumbents already advertise source-linked answers and financial data connectors (E32), though independent verification is missing.
- Benchmarks use older models; 2026-model error shares are unmeasured `[GAP]`.
- The only demand-side evidence is a vendor survey without methodology (E21) and anecdotes (E30).
- Higher accuracy may not translate to trust or efficiency without workflow integration `[HYP]`.

## 6. What this research cannot establish

- Whether analysts experience these failures frequently enough to pay for a fix.
- The relative contribution of parsing vs retrieval vs reasoning in current systems.
- That any existing vendor lacks the proposed controls (see [competitive-landscape](competitive-landscape.md)).
- Any efficiency gain: no time-and-motion measurement exists in the evidence base.

## 7. Conclusion for the problem stage

The *technical* problem is real and documented in parts. The *user and market* problem is plausible but unvalidated, and the PDF-specific part of it is likely concentrated in a narrower segment than "financial analysts" generally. This supports narrowing and validating before building. See the README for the recommendation.
