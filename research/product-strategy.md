# Product Strategy: Use-Case Selection, Hypothesis, Decision

Added to the proposed repository structure because the use-case selection, product hypothesis and decision have no other home. Evidence IDs refer to [../evidence-register.md](../evidence-register.md).

## 1. Candidate use cases

| ID | Use case |
|---|---|
| UC1 | Comparing financial statement figures across reporting periods |
| UC2 | Extracting and validating financial metrics from annual reports into a structured template |
| UC3 | Answering analyst questions that need calculations across tables and narrative |
| UC4 | Reconciling figures across multiple documents |

## 2. Selection criteria and scoring

Scores are 1 (worst) to 5 (best) and are **my judgments, AI-assisted and not validated with users**. Weights sum to 100 and were chosen before scoring but are subjective. The point of the table is to make reasoning inspectable and open to challenge, not to produce a decisive number. Weighted score = Σ(weight × score) / 100, computed by script.

| Criterion | Weight | UC1 | UC2 | UC3 | UC4 | Rationale for the scores |
|---|---:|---:|---:|---:|---:|---|
| Severity of user problem | 15 | 3 | 4 | 4 | 4 | Cross-period tasks degrade (E15); reconciliation errors are costly; severity unmeasured for users |
| Frequency of workflow | 10 | 4 | 5 | 4 | 3 | Extraction recurs in every filing cycle `[INF]` |
| Consequence of errors | 10 | 3 | 4 | 3 | 5 | Reconciliation/audit contexts carry higher stakes `[INF]` |
| Availability of credible evidence | 15 | 3 | 3 | 4 | 2 | UC3 has benchmarks (E01, E02, E04); UC4 has little; UC1 has Fin-RATE (E15) |
| Technical feasibility | 10 | 4 | 4 | 2 | 2 | UC2 is bounded and checkable; UC3 and UC4 need open-ended reasoning and entity matching |
| Evaluation feasibility | 15 | 4 | 5 | 3 | 2 | UC2 has ground truth via XBRL for public filers (E25) and a clean cell-level metric; UC4 lacks labeled data |
| Integration & security requirements | 5 | 4 | 4 | 3 | 2 | Higher score = easier; UC4 needs multi-document access control |
| Potential economic value | 10 | 3 | 3 | 4 | 4 | Unvalidated; broader tasks may be worth more but unproven |
| Competitive differentiation | 10 | 2 | 2 | 1 | 3 | UC3 is crowded (E32); UC2/UC1 overlap structured-data vendors (E32, E25); UC4 less marketed in sources I read, not confirmed absent |
| **Weighted score** | 100 | **3.3** | **3.8** | **3.2** | **3.0** | |

**Sensitivity check:** UC2's lead comes mostly from frequency, evaluation feasibility and technical feasibility. If differentiation weight were raised, UC4 would gain; I did not run a formal weight sweep. `[GAP]`

## 3. Selected narrow initial use case (provisional)

**UC2 restricted to non-XBRL documents:** extract and validate a defined set of financial-statement metrics (e.g., revenue, operating income, total assets, with units and periods) from financial-statement PDFs that **lack** a free structured source, then support period-over-period comparison (a narrow slice of UC1).

Why this and not the more "interesting" UC3/UC4: it can be evaluated with a cell-level ground truth; it reduces the intervention to components that have evidence behind them (table structure, units/period, rule checks); it avoids a head-on fight with source-linked Q&A incumbents (E32); and public-filer XBRL data (E25) provides a verification oracle for a *proxy* benchmark. Why restricted to non-XBRL: for XBRL filers the structured data makes PDF parsing unnecessary, so a PDF-first product there lacks a clear rationale.

Weakness: the non-XBRL slice is exactly where ground truth and public documents are hardest to obtain, so the experiment will need synthetic or de-identified material, and the real-world importance of the slice is unverified.

## 4. Product hypothesis

| Element | Statement |
|---|---|
| Target user | Analysts in credit, diligence or research teams who spread financials from PDFs that have no structured source `[HYP]` |
| Job to be done | "Get the specific figures I need, for the right entity, period, unit and basis, with proof I can check quickly" |
| Current workflow | Manual transcription or copy-paste into Excel, possibly assisted by general chat tools, followed by manual tie-out `[INF]`, unobserved |
| Pain point | Time spent transcribing and verifying; silent errors in period/unit/column mapping `[HYP]` |
| Intervention | Structure-aware parsing with explicit unit/period/footnote capture; deterministic computation of derived figures; rule-based validation; span-level provenance; abstention on failed checks |
| Expected measurable outcome | Lower false-acceptance rate and lower human correction time than the best plain-RAG baseline, at acceptable abstention; thresholds in the [evaluation plan](evaluation-plan.md) |
| Key assumptions | (1) the segment exists and is large enough; (2) parsing/structure is a material loss source for these documents (E14 casts doubt for text-first parsers on general financial PDFs); (3) rule checks catch a meaningful share of errors; (4) users trust and adopt verified output; (5) data can be processed within security constraints |
| Evidence needed to validate | Interviews with target users (workflow, error experience, tool budgets); a measured baseline error profile on representative documents; the offline experiment; a pricing/willingness-to-pay probe |

**Why it could differ from existing assistants (hypothesis, not a finding):** the proposition would be *measured* reliability with abstention on a defined document class, plus reproducible public evaluation, rather than broader coverage or more citations. This is only meaningful if tests show incumbents' accuracy on that class is lacking; those tests have not been done.

## 5. Strategic options compared

| Option | Basis | Risk |
|---|---|---|
| Proceed to a limited prototype | Technical failures are documented | Demand unvalidated; incumbents; PDF premise contested (E14, E25) |
| **Conduct further problem validation** | Demand and segment unvalidated; evidence thin on workflow | Delay; may confirm no problem |
| Narrow the target use case | Done in §3 | Narrow slice may be too small |
| Change the solution (e.g., integrate XBRL + data vendors) | Free structured data exists | Becomes a data-product, crowded |
| Do not pursue | Competition, weak demand evidence | May forgo a real gap in a niche |

## 6. Decision

**Recommendation: Conduct further problem validation** on the narrowed hypothesis in §3 (non-XBRL financial-statement PDFs), with two parallel, inexpensive evidence-gathering activities and **no product build**:

1. **Primary problem validation** (not yet done): 8–12 structured interviews with analysts in credit/diligence/research who handle non-structured financial documents, covering workflow, error experiences, tools in use, budgets, and security constraints. Requires recruiting, consent and a disclosure of any AI use in the research process to participants.
2. **Offline reliability experiment** (the [evaluation plan](evaluation-plan.md)), run as a research experiment, not a product, to find where errors actually come from. Its outcome can change the decision either way.

**Why not "proceed to a prototype":** there is no demand-side evidence; the literature does not show that structure-aware parsing is the main lever (E14); free structured data exists for the largest public-company segment (E25); and incumbents already advertise source-linked answers (E32), unverified but plausible.

**Why not "do not pursue":** the technical failure modes are documented (E04, E15, E16), citation faithfulness is a known weak point in adjacent systems (E09, E10), and an unevaluated, open comparison in a niche segment is a legitimate gap in the evidence base.

**Strongest counterarguments**
- Frontier models with long context may already read financial PDFs well enough that a pipeline adds little (E22/E23 suggest strong LLM parsing; E04 shows long context helped).
- Verification effort may be dominated by policy, not accuracy, so gains are capped `[HYP]`.
- A small niche might not support the fixed costs (see [economic model](economic-model.md)).
- My segment inference could be wrong.

**Unresolved uncertainties:** user demand; real error rates of current commercial tools; share of loss by pipeline stage; minutes saved per document; willingness to pay.

**Evidence that would change the decision**
- *Toward a prototype:* interviews show recurring, costly, un-served extraction/verification work; the experiment shows I beats B-best by the pre-set margin with low false acceptance; at least some buyers confirm budget.
- *Toward stopping:* B2 (frontier model, no pipeline) or cheap-parser RAG matches I; interviewees rely on structured data or already-accepted tools; no one will commit time or budget.
- *Toward changing the solution:* the main loss sits in retrieval/reasoning rather than parsing, or users need reconciliation across documents more than extraction.
