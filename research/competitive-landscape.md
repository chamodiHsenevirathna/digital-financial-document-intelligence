# Competitive Landscape

Evidence IDs refer to [../evidence-register.md](../evidence-register.md).

**Method and limits.** I read vendor/product pages and repositories (WEB/GH) or search-result summaries (SNIP). I did **not** trial any product, request demos, read security whitepapers, or obtain pricing. Therefore every capability below is *claimed or described*, not verified. Cells marked "Not found" mean I did not find a statement in the pages I read. They do **not** mean the capability is absent. Nothing here supports a claim that a capability is missing from the market.

## 1. Categories

| Category | Examples (non-exhaustive) | What it is for |
|---|---|---|
| A. PDF/document parsers (open source) | Docling (E12), Unstructured, pdfplumber, PyMuPDF, pdfminer, Marker | Convert PDFs to text/tables/layout; building blocks |
| B. Commercial parsing/IDP APIs | LlamaParse (E27), Azure Document Intelligence, AWS Textract, Google Document AI | Managed OCR/layout/table extraction |
| C. RAG frameworks | LlamaIndex, LangChain, etc. | Assemble retrieval pipelines (not evaluated here) |
| D. Finance-specific AI research platforms | Hebbia, Rogo, AlphaSense, Brightwave, Claude for Financial Services (E32) | Q&A and workflows over filings, transcripts, proprietary docs |
| E. Structured financial data providers | Daloopa (E32), SEC EDGAR XBRL APIs (E25), FactSet/S&P/others | Normalized figures, often with source links |
| F. General assistants | ChatGPT, Claude, Copilot-type tools | Flexible Q&A; user uploads PDFs |

## 2. Capability comparison (as claimed/described)

Legend: ✔ stated in a source I read · ~ partial/indirect · ? not found in sources read · n/a not the product's purpose. "Source" = evidence ID.

| Capability | Docling (A) | LlamaParse / Azure DI (B) | Hebbia (D) | Claude for Fin. Services (D) | Daloopa (E) | SEC XBRL API (E) |
|---|---|---|---|---|---|---|
| Document parsing & table extraction | ✔ layout (DocLayNet) + TableFormer (E12) | ✔ parsing modes; accuracy unverified (E22/E27) | ? (grid over sources; method not found) | ? | ✔ pipeline claims (vendor) | n/a (pre-tagged) |
| Retrieval quality | n/a | n/a | ~ "Iterative Source Decomposition" (SNIP, third-party) | ? | n/a | n/a |
| Numerical reasoning | n/a | n/a | ? | ✔ claims via Excel/agents (vendor; 83% on Excel tasks, methodology not given) | n/a | n/a |
| Citation/provenance | ~ (export formats; provenance not confirmed on page read) | ~ | ~ "Source Documents" column in sample; sentence-level citation claimed in vendor-authored comparison (SNIP) | ✔ "every claim links directly to its original source" (claim) | ✔ each data point hyperlinked to filing (vendor claim, SNIP) | ~ XBRL disclosures per company and concept via API (official, E25); filing-level linkage not confirmed on the page I read |
| Deterministic calculation & validation | n/a | n/a | ? | ~ Excel formulas/cell citations (SNIP, secondary) | ✔ normalized datasets (claim) | ✔ structured values |
| Uncertainty/conflict handling | n/a | n/a | ? | Page states "cross-checked across sources"; no limitations stated | ? | n/a |
| Privacy/security controls | local/self-host (MIT-licensed code) | cloud API | "Security" section linked, content not read | Data "not used for training by default" (claim) | ? | public data |
| Integration complexity | Python library; developer effort | API; developer effort | Demo/enterprise sale | Enterprise plans + connectors | Subscription/connectors (Hebbia, Rogo, Glean, Gemini Enterprise) | Free HTTP API, developer effort |
| Cost/suitability | Free software; compute and engineering cost | Credit pricing: $1.25 per 1,000 credits; credits/page vary by mode (E27); Azure price not retrieved | No pricing; "Request a demo" | Not found | Not found | Free, no key required (E25) |

## 3. What the evidence supports

1. **Source-linked answers are already marketed by several vendors** (Anthropic, Daloopa, Hebbia-related material). I did not test whether the links are accurate. The legal-RAG study (E09) and citation study (E10) show vendor claims and citation presence can diverge from correctness, so a test is warranted, but that is a hypothesis about finance products `[HYP]`, not a finding.
2. **Structured data is a strong substitute for PDF parsing for US-listed companies** (E25, E32). Any PDF-parsing product competes with a free structured source on that segment.
3. **Parser performance claims are inconsistent and mostly vendor-run.** Unstructured's own benchmark ranks itself first (E23); an unattributed GitHub benchmark ranks pdfplumber highest on table TEDS but includes no financial statements (E22); a blog summary favors Docling on sustainability reports (E24). No independent benchmark on financial-statement tables was found `[GAP]`.
4. **Frontier LLMs are themselves parsers.** E22 reports GPT-5.1 leading edit similarity (at higher cost per page), and E23 reports frontier models scoring well on its tasks. This weakens an assumption that dedicated structure-aware parsers are always necessary, and it raises the baseline the intervention must beat.
5. **No independent head-to-head of financial assistants** was found `[GAP]`. The only evaluations are benchmark papers on general-purpose models (E04, E15) and self-reported system papers (E17).

## 4. Differentiation: what could and could not be different

Could be different (all `[HYP]`, to be tested, not claimed):
- **Verification-first behavior**: deterministic recomputation with explicit unit/period/basis checks and *abstention* as a first-class output, reported with measured false-acceptance rates.
- **Open, reproducible evaluation**: published ablations isolating which component matters (the literature mostly reports whole-system numbers).
- **Local/private operation** using open-source components, relevant where documents cannot leave the firm (unverified need).
- **Focus on non-XBRL documents**, where structured sources do not exist.

Not different (do not claim as differentiators): citations to source pages, table-aware chunking, "agentic" retrieval, calculator tool use. All are described by existing products or papers (E17, E32, E07/E08).

## 5. Implication

A new product would not win on "cites its sources" or "reads tables." It could only justify itself by **demonstrated reliability on a defined document class** plus **workflow fit and security posture** that incumbents do not provide for that class. Both are unproven here. This is the principal reason for the "validate before building" recommendation in the README.

## 6. Open-source "build vs integrate"

If any prototype were built, the evidence favors **integrating** existing components (Docling or pdfplumber/pdfminer for parsing, per E12/E14; a standard hybrid retriever; Python for arithmetic) rather than building new ones, and spending effort on the evaluation harness and verification layer.
