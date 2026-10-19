# Evidence Register

All sources accessed **2026-10-19**. "Inspection depth" records what was actually read, because many entries were verified from an abstract or web page only. AI assistance was used to retrieve and summarize pages (see [methodology/ai-use-and-research-limitations.md](methodology/ai-use-and-research-limitations.md)); no figure below was taken from memory without a retrieved source.

**Confidence scale** (confidence that the entry supports the *specific finding stated*, not the product idea): High = primary source, finding stated directly, methodology credible. Medium = primary source but abstract-only, vendor-adjacent, or narrow setting. Low = secondary summary, vendor claim, or anecdote.

**Inspection depth codes:** `FULL` = body text read (in part; see note), `ABS` = arXiv/abstract page only, `WEB` = product/docs page only, `SNIP` = only a search-result summary (source page not opened), `GH` = GitHub README page.

**Evidence status codes** used in the research files: `[EST]` established finding, `[CON]` conflicting evidence, `[INF]` reasonable inference, `[HYP]` unverified hypothesis, `[GAP]` missing evidence.

---

## A. Benchmarks and datasets

### E01 — FinQA
- **Claim/question:** Do pre-trained models perform multi-step numerical reasoning over financial reports as well as experts?
- **Source:** Chen et al., "FinQA: A Dataset of Numerical Reasoning over Financial Data." EMNLP 2021. https://arxiv.org/abs/2109.00122 · Repo: https://github.com/czyssrs/FinQA
- **Date:** 2021-09-01 (v3 2022-05-07). **Type:** peer-reviewed dataset paper. **Depth:** ABS + GH.
- **Finding:** Large pre-trained models "fall far short of expert humans" (abstract gives no numbers). Repo license: MIT.
- **Setting/limits:** Expert-written questions over financial reports (company reports, per repo IDs). 2021-era models, so the gap is likely smaller for current LLMs. Split sizes not verified by me.
- **Confidence:** Medium. **Decision effect:** Suitable component-level benchmark (table+text numerical reasoning); not evidence about current frontier models.

### E02 — TAT-QA
- **Source:** Zhu et al., "TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance." ACL 2021. https://arxiv.org/abs/2105.07624 · https://github.com/NExTplusplus/TAT-QA
- **Date:** 2021-05-17. **Type:** peer-reviewed dataset. **Depth:** ABS + GH.
- **Finding:** Best model then (TAGOP) 58.0% F1 vs expert humans 90.8% F1. Repo reports 16,552 questions over 2,757 hybrid contexts; dataset license CC BY 4.0, code MIT.
- **Limits:** 2021-era result; contexts are pre-extracted table+text, so it does **not** test PDF parsing.
- **Confidence:** Medium (high for dataset facts, low relevance of the F1 gap to 2026 systems). **Effect:** Candidate for isolating reasoning/calculation from parsing.

### E03 — ConvFinQA
- **Source:** Chen et al., "ConvFinQA." EMNLP 2022. https://arxiv.org/abs/2210.03849
- **Date:** 2022-10-07. **Depth:** ABS. **Finding:** Analyzes neural-symbolic and prompting methods for conversational numerical reasoning (no numbers in abstract). Dataset license not checked.
- **Confidence:** Medium. **Effect:** Lower priority; conversational chaining is beyond the initial scope.

### E04 — FinanceBench
- **Source:** Islam et al. (Patronus AI), "FinanceBench: A New Benchmark for Financial Question Answering." https://arxiv.org/abs/2311.11944 · https://github.com/patronus-ai/financebench
- **Date:** 2023-11-20. **Type:** preprint/benchmark by an evaluation vendor. **Depth:** ABS + GH; additional quoted figures via SNIP of paper text (full paper not opened).
- **Finding (ABS):** 10,231 questions on public companies; 16 configurations tested on a 150-case sample; 2,400 answers manually reviewed; GPT-4-Turbo with a retrieval system "incorrectly answered or refused to answer 81% of questions" (abstract; the "shared vector store" detail and the following figures are **SNIP, unverified by me**): long-context configurations scored ~76–79% correct with 17–21% hallucination; placing the filing before the question raised GPT-4-Turbo from 25% to 78%.
- **Limits:** 2023 models and retrieval setups; only 150 questions are open; the repo page states no license (I could not confirm reuse terms). Authors describe questions as clear-cut, a "minimum performance standard."
- **Confidence:** Medium. **Conflict:** Mimir (E17) reports 89.3% on the same benchmark with a table-aware pipeline, so the 81% figure describes a 2023 baseline, not the state of the art. **Effect:** Core end-to-end benchmark; the 150-question sample is the only openly available part.

### E05 — DocFinQA
- **Source:** Reddy et al. (Kensho), "DocFinQA: A Long-Context Financial Reasoning Dataset." ACL 2024. https://arxiv.org/abs/2401.06915
- **Date:** 2024-01-12 (v3 2025-10-24). **Depth:** ABS.
- **Finding:** 7,437 FinQA questions augmented with full SEC-filing context (average context from <700 words to ~123k words); "significant challenge for even state-of-the-art systems"; worst on longest documents.
- **Limits:** License not checked. Context is parsed text of filings, so it exercises retrieval and long context but not PDF layout.
- **Confidence:** Medium. **Effect:** Candidate for the retrieval ablation.

### E15 — Fin-RATE
- **Source:** Jiang et al., "Fin-RATE: A Real-world Financial Analytics and Tracking Evaluation Benchmark for LLMs on SEC Filings." KDD 2026. https://arxiv.org/abs/2602.07294 · https://huggingface.co/datasets/GGLabYale/Fin-RATE
- **Date:** 2026-02-07 (v4 2026-06-10). **Depth:** ABS + FULL (first pages read; 7,500 questions confirmed in text; error-taxonomy tables not read).
- **Finding:** 17 LLMs benchmarked with ground-truth context and retrieval-augmented settings. Accuracy fell 18.60% (to longitudinal tracking) and 14.35% (to cross-entity analysis) relative to single-document reasoning, associated with comparison hallucinations and temporal/entity mismatches. Introduces a 13-type error taxonomy to separate retrieval, generation and reasoning errors.
- **Limits:** The paper describes a human-consistency check on 4,500 instances, which suggests LLM-based judging; I did not read the details. Two authors are affiliated with Goldman Sachs (disclosed in paper header); no evidence of bias found, noted for transparency.
- **Confidence:** Medium-High. **Effect:** Strongest peer-reviewed signal that cross-period analysis is harder than single-fact lookup, supporting a period-comparison use case. It tests LLMs on filings text, not PDF layout.

### E16 — FinIndices
- **Source:** Tong et al., "Are the Financial Reasoning from LLMs Credible? A Real World Test over Long-Horizon Statements." https://arxiv.org/abs/2607.28661
- **Date:** 2026-07-22. **Depth:** ABS.
- **Finding:** On uncropped statements up to 32K tokens, Gemini-3.1-Pro fell from 70.70% to 38.22% on table tasks when formula hints were removed ("fragile pattern matching"); multi-metric, multi-period tables induced shortcuts "such as pulling data from incorrect adjacent columns." SFT gave +8.54 / +3.82 points.
- **Limits:** Preprint, abstract only, 3 months old, not peer reviewed. **Confidence:** Low-Medium. **Effect:** Supports the column/period-misalignment failure hypothesis and the need for deterministic formulas.

---

## B. Technical studies on parsing, chunking, retrieval, reasoning

### E14 — Empirical Evaluation of PDF Parsing and Chunking for Financial QA with RAG
- **Source:** El Bachyr et al. (Univ. of Luxembourg, BGL BNP Paribas), ICSE-SEIP 2026. https://arxiv.org/abs/2604.12047
- **Date:** 2026-04-13. **Depth:** FULL (abstract, method summary, threats to validity and conclusion read; result heatmaps not reliably machine-readable and **not** quoted numerically).
- **Finding:** On FinanceBench and the authors' new TableQuest (table-focused, GPT-4o-generated questions with automatic validation), six open-source parsers (PyPDF2, PyMuPDF, pdfminer.six, pypdfium2, pdfplumber, Unstructured), six chunkers, four retriever families, and twelve LLMs were compared. Conclusions as stated: (1) retriever and parser choices matter strongly, "with lightweight combinations often matching more complex ones"; (2) moderate chunk overlap helps, excessive granularity adds cost without consistent benefit; (3) larger LLMs boost correctness but gains level off beyond medium scale. The paper states pdfminer is the best default for narrative financial documents and pdfplumber is preferable when tables dominate.
- **Limits (authors):** single seed; LLM-as-judge (gpt-4o-mini) shares biases with generators; two datasets; no table-structure-recognition parser such as Docling (TableFormer) in the compared set (Unstructured, which the paper describes as using OCR and model-based layout detection, was included); page-level retrieval.
- **Confidence:** High for what it tested. **Conflict:** pushes against "structure-aware parsing is the main lever": cheap parsers were often competitive. **Effect:** Reduces the prior that parsing is the dominant failure source; mandates an ablation instead of an assumption.

### E06 — Financial Report Chunking
- **Source:** Jimeno Yepes et al., https://arxiv.org/abs/2402.05131 · **Date:** 2024-02-05 (v3 2024-03-16). **Depth:** ABS.
- **Finding:** Chunking by document structural elements "largely improve[s] RAG results on financial reporting" vs paragraph-level chunking. No numbers in abstract; baseline is paragraph chunking only.
- **Confidence:** Medium. **Effect:** Supports structure-aware chunking as a hypothesis to test.

### E13 — Multi-structured financial documents with pre-processing
- **Source:** Upadhyay et al., https://arxiv.org/abs/2506.05182 · **Date:** 2025-06-05 (v2 2025-08-20). **Depth:** ABS.
- **Finding:** GPT-4o 56% accuracy given documents directly; with pre-processing 61.3% (GPT-4o) and 76% (GPT-4). LLMs err on nested tables and multi-dimensional plots.
- **Limits:** Dataset and tools not described in the abstract; the gains are not attributed to a specific component. **Confidence:** Medium-Low. **Effect:** Directional support for pre-processing.

### E17 — MimirRAG
- **Source:** Samuelsen et al., https://arxiv.org/abs/2605.25030 · **Date:** 2026-05-24. **Depth:** ABS.
- **Finding:** Multi-agent RAG reaches 89.3% on FinanceBench; authors credit metadata integration, table-aware chunking and an agentic workflow; four financial analysts gave qualitative validation, emphasizing "calibrated trust".
- **Limits:** Self-reported; baselines and ablation numbers not in abstract; four evaluators. **Confidence:** Low-Medium. **Effect:** Shows a combined pipeline can score high on FinanceBench; does not isolate which element helped (I did not read the ablation).

### E07 — Program of Thoughts / E08 — PAL
- **Sources:** Chen et al., https://arxiv.org/abs/2211.12588 (TMLR 2023); Gao et al., https://arxiv.org/abs/2211.10435 (2022). **Depth:** ABS.
- **Finding:** Offloading computation to an interpreter gave ~12% average gain over chain-of-thought across math and financial QA datasets (FinQA, ConvFinQA, TATQA) in PoT; PAL beat PaLM-540B CoT by 15% absolute on GSM8K.
- **Limits:** 2022-era models; today's models do arithmetic better, so the margin is uncertain. **Confidence:** High (for 2022 models). **Effect:** Supports deterministic computation as a design principle; margin for current models is a `[GAP]`.

### E28 — Seven Failure Points (RAG)
- **Source:** Barnett et al., https://arxiv.org/abs/2401.05856 · **Date:** 2024-01-11. **Depth:** ABS (the seven points are in the body; I did not read them).
- **Finding:** Experience report from three case studies (research, education, biomedical); validation is only feasible in operation and robustness evolves over time. **Confidence:** Medium. **Effect:** Frames failure taxonomy; not finance-specific.

### E11 — Lost in the Middle
- **Source:** Liu et al., https://arxiv.org/abs/2307.03172 (TACL) · **Date:** 2023-07-06. **Depth:** ABS.
- **Finding:** Performance degrades when relevant information is in the middle of long inputs. **Limits:** 2023 models. **Confidence:** High (then). **Effect:** Context-assembly risk; the extent for current models is a `[GAP]`.

### E20 — FRED
- **Source:** Tan et al., https://arxiv.org/abs/2507.20930 · **Date:** 2025-07-28. **Depth:** ABS.
- **Finding:** Fine-tuned models detect injected errors in financial QA output: best (Phi-4) +8% binary F1 and +30% overall detection vs OpenAI-o3. Synthetic injected errors.
- **Confidence:** Low-Medium. **Effect:** A learned verifier is possible but synthetic-error evaluation may not reflect real errors.

### E22 — PDF-Bench (GitHub)
- **Source:** https://github.com/applied-artificial-intelligence/pdf-parser-benchmark · **Depth:** GH.
- **Finding:** 353 documents (legal contracts, invoices, résumés, papers, synthetic tests); no financial statements. pdfplumber 93.4% TEDS on tables; GPT-5.1 92% edit similarity at ~$0.05/page; LlamaParse 78% at ~$0.003/page; "text accuracy averages 74% but structure preservation only 35%." Authorship unclear (hosted under an organization; README points to another account).
- **Confidence:** Low. **Effect:** Cost anchors for the economic model only; **not** evidence about financial PDFs.

### E23 — Unstructured benchmarks
- **Source:** https://unstructured.io/benchmarks · **Depth:** WEB. Vendor-run; asymmetric tuning (multiple configs for some tools, defaults for others); date not shown.
- **Finding:** Unstructured ranks itself first on text fidelity and table cell accuracy (0.880 / 0.820). **Confidence:** Low (conflict of interest). **Effect:** None beyond showing vendor benchmarks disagree with others.

### E24 — Procycons parser comparison
- **Source:** https://procycons.com/en/blogs/pdf-data-extraction-benchmark/ · **Depth:** SNIP only. Reported Docling strongest on complex tables in *sustainability reports*; figure of 97.9% is possibly vendor-sourced per the search summary. **Confidence:** Low. **Effect:** none; recorded to show that parser rankings are inconsistent across sources.

### E12 — Docling
- **Sources:** Auer et al., https://arxiv.org/abs/2408.09869 (2024-08-19); https://github.com/docling-project/docling · **Depth:** ABS + GH.
- **Finding:** MIT-licensed open-source PDF converter using DocLayNet layout analysis and TableFormer table structure; exports Markdown/HTML/JSON; hosted by LF AI & Data, started by IBM Research. No accuracy numbers verified by me. GH page did not mention bounding boxes/provenance (not confirmed either way).
- **Confidence:** High for existence/features. **Effect:** Realistic open-source baseline/intervention component.

---

## C. Reliability of AI with citations (adjacent domains)

### E09 — Hallucination in legal AI research tools
- **Source:** Magesh et al., https://arxiv.org/abs/2405.20362 · **Date:** 2024-05-30. **Depth:** ABS.
- **Finding:** Preregistered evaluation; Lexis+ AI and Westlaw tools hallucinate 17–33% of the time, less than general chatbots but contrary to vendor "hallucination-free" claims.
- **Limits:** Legal domain, 2024 products. **Confidence:** High (for legal). **Effect:** Analogy only: RAG with citations does not eliminate errors, and vendor claims need independent testing. `[INF]` for finance.

### E10 — Verifiability in generative search engines
- **Source:** Liu, Zhang, Liang, https://arxiv.org/abs/2304.09848 · **Date:** 2023-04-19. **Depth:** ABS.
- **Finding:** Across four engines, 51.5% of sentences were fully supported by citations (citation recall) and 74.5% of citations supported their sentence (precision).
- **Limits:** 2023 products, general web queries. **Confidence:** High (then). **Effect:** Citations can look authoritative while failing to support claims; supports measuring citation support rather than assuming it.

### E19 — GPT as sell-side analysts
- **Source:** Li et al., https://arxiv.org/abs/2412.01069 · **Date:** 2024-12-02 (v2 2025-10-22). **Depth:** ABS.
- **Finding:** GPT's numerical reasoning varies widely by context; "the locus of friction may shift from processing information to evaluating model outputs."
- **Confidence:** Medium. **Effect:** Supports verification cost as a central issue; an `[INF]`, not a measurement of analyst time.

---

## D. Market, demand and workflow signals

### E21 — Datarails CFO survey (via ITPro)
- **Source:** https://www.itpro.com/business/business-strategy/finance-teams-are-wasting-a-quarter-of-their-week-checking-ai-slop (article dated 2026-10-08), reporting Datarails' 2026 CFO Sentiments Survey. **Depth:** WEB (secondary).
- **Finding as reported:** n=270 CFOs; teams spend 26% of the working week checking AI output; ~96% of CFOs spend at least 10% of time checking or fixing AI output; 8% more than half.
- **Limits:** Vendor-run survey; no methodology, field dates, recruitment or question wording available; the article is secondhand. Concerns AI output generally, not PDF analysis.
- **Confidence:** Low. **Effect:** Weak, vendor-motivated signal that verification burden exists; **not** used as an input to the economic model.

### E30 — Practitioner signals (non-Reddit)
- **Sources:** CFO Impulse Substack "How ChatGPT fails at data analysis" https://cfoimpulse.substack.com/p/finance-impulse-how-chatgpt-fails (one practitioner's tests; Python analysis described as a "black box"); a single Capterra ChatGPT review snippet ("if i don't check twice, it gives me wrong numbers sometimes"). **Depth:** SNIP only.
- **Confidence:** Low (anecdotes). **Effect:** Qualitative problem signal only.
- **Reddit:** Three searches did not surface any retrievable Reddit thread on this topic. **No Reddit evidence is cited.** `[GAP]`

### E32 — Vendor claims (not independent evidence)
- **Claude for Financial Services (Anthropic):** https://www.anthropic.com/news/claude-for-financial-services (2025-07-15). WEB. Claims "every claim links directly to its original source"; names connectors (FactSet, S&P Global, PitchBook, Morningstar, Daloopa, etc.). The page states no limitations and gives no independent validation of its performance claims. Excel-add-in details come from SNIP secondary pages only.
- **Hebbia:** https://www.hebbia.com/ WEB. Grid product (Matrix) with a "Source Documents" column; the page I read makes no explicit accuracy/citation claim; no pricing. Sentence-level-citation claims appear in Hebbia-authored comparison pages (SNIP, vendor-authored).
- **Daloopa:** SNIP (vendor/partner pages): says every datapoint hyperlinks to its source filing; "99%+" accuracy is the company's own claim; coverage figures vary by source (4,700–6,000+ companies). https://fintech.global/2026/05/28/daloopa-raises-47m-to-fix-ais-financial-data-problem/
- **Rogo:** SNIP: reported $160M Series D (April 2026) and ~$50M ARR via secondary press; unverified.
- **Confidence:** Low. **Effect:** Establishes that traceability to source is already a marketed feature at several vendors. Capabilities are **unverified** by me.

---

## E. Data availability, security and cost

### E25 — SEC EDGAR APIs (official)
- **Source:** https://www.sec.gov/search-filings/edgar-application-programming-interfaces · **Depth:** WEB.
- **Finding:** data.sec.gov provides submissions, XBRL companyconcept, companyfacts and frames JSON APIs, plus nightly bulk ZIPs; "These APIs do not require any authentication or API keys"; XBRL APIs typical delay under a minute.
- **Effect (important):** For US-listed filers, structured XBRL facts exist for free, so PDF parsing is not the only route to financial values. The PDF problem is strongest for documents *without* XBRL (private companies, non-US filers without equivalent tagging, supplements, presentations, lender/diligence packages, scanned statements). Coverage and quality of those tags were not evaluated here. `[GAP]`

### E26 — OWASP LLM01 Prompt Injection
- **Source:** https://genai.owasp.org/llmrisk/llm01-prompt-injection/ · **Depth:** WEB (official).
- **Finding:** Indirect injection occurs when an LLM ingests external content (files, websites) containing instructions. Mitigations: constrain behavior, validate output formats deterministically, filter inputs/outputs, least privilege, human approval for high-risk actions, segregate untrusted content, adversarial testing. OWASP notes it is "unclear if there are fool-proof methods of prevention."
- **Confidence:** High. **Effect:** Uploaded filings and third-party PDFs are untrusted input; mitigations reduce impact only.

### E27 — Parsing prices
- **LlamaIndex pricing:** https://www.llamaindex.ai/pricing · WEB · 1,000 credits = $1.25; basic parsing "as low as 1 credit"; agentic modes cost more; credits per page per mode not stated on the page I read.
- **Azure Document Intelligence:** https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/ · WEB · the fetched page showed placeholders ("$-") instead of prices; free tier of 500 pages/month; **no price recorded**. `[GAP]`
- **Confidence:** High for the LlamaIndex credit price (as of access date); prices change.

---

## Excluded sources

- **"Agentic Retrieval-Augmented Generation for Financial Document Question Answering"** (https://arxiv.org/abs/2605.05409): withdrawn by its authors on 2026-07-05 for "significant methodological errors"; none of its numbers are used.
- **arXiv 2401.17167** was initially mis-guessed as DocFinQA; it is UltraTool (tool-use benchmark) and is not used.
- Blog posts claiming unsourced statistics (e.g., a DEV Community claim that "68% of financial extraction errors are hallucinated numbers") were not used.

## Evidence still missing (`[GAP]`)

1. Any direct observation of analyst workflows (no interviews or surveys were conducted).
2. Independent head-to-head accuracy data for commercial financial assistants (Hebbia, Rogo, AlphaSense, Claude for Financial Services, Copilot) on a shared task.
3. Parser accuracy on **financial-statement tables specifically**, from a non-vendor source (E22, E23, E24 are inadequate).
4. Share of real-world errors attributable to parsing vs retrieval vs reasoning in finance (Fin-RATE's taxonomy tables were not read).
5. Willingness to pay; budgets; procurement constraints.
6. Evidence on how often deterministic checks (e.g., sub-totals, balance-sheet identity) catch extraction errors in real filings.
7. Current-generation (2026) model performance on FinanceBench-style tasks with a reproducible harness.
