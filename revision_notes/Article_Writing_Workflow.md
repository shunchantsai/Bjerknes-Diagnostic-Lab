# Article Writing Workflow (v1) — "Verify, then Write"

*For the El Niño / catastrophe-risk article (Google Docs). Companion to the notebook deep-read workflow.*

**Date started:** 2026-07-07

---

## The one rule

This article is a portfolio piece — primary signal for **CAT-modeling roles**, transferable signal for a
**flood-risk PhD** (physical geography, climate science, project management). Its credibility rests on the
same standard as the notebooks:

> **No load-bearing claim survives in the text without a verified primary source. Wrong citations are worse
> than missing ones. Claude's assertions are not a source.**

Everything below exists to enforce that rule without slowing you into paralysis.

---

## The five disciplines (carried from the notebook workflow)

1. **Verify before asserting** — every number, forecast probability, historical figure, and citation is checked against a primary source before it stays.
2. **One scope per session** — a sitting is *one* type of work, never a blend (see Session Types).
3. **Before/After edits** — changes are made instance-by-instance as OLD → NEW, not by rewriting whole passages from memory.
4. **Hold list** — facts that can't be verified *yet* live in a HELD list with a trigger, never as bare claims in the prose.
5. **Log every session** — a running Revision Log is the article's CHANGELOG.

---

## Session types — declare ONE at the start, never mix

| Type | You do | You do NOT |
|---|---|---|
| **READ / COLLECT** | read sources, take notes, populate the Sources Ledger | write article prose |
| **DRAFT** | write new prose from the section plan; tag every fact `[verify: source]` inline | fact-check or restructure |
| **VERIFY** | resolve `[verify]` tags against primary sources → CONFIRMED or HELD | write new prose |
| **RESTRUCTURE** | reorder, cut, tighten existing prose; fix flow/signposting | add new claims or new facts |

Mixing types is how a "quick edit" becomes an untracked rewrite with unverified numbers. If mid-session you
spot the *other* kind of work, log it and move on — don't do it now.

---

## The per-session loop

0. **Anchor** — one sentence: *"This session is a [TYPE] pass on [section]."* Write it at the top of your notes.
1. **Do the scoped work** for that type only.
2. **DRAFT rule:** never write a bare number. Every fact enters as `+1.7 °C [verify: IRI Quick Look, June 2026]` — the claim and its candidate source together. A sentence with an un-tagged number is a bug.
3. **VERIFY rule:** open the primary source, confirm the exact figure, then either
   - **CONFIRM** → replace the tag with the real citation, log it in the Sources Ledger, or
   - **HOLD** → move the item to the Hold List with a trigger date/event; leave a visible `[HELD: …]` marker in the text.
4. **Log** — one line in the Revision Log; update the Sources Ledger / Hold List.
5. **Close (two-minute reconcile pass)** — tick what's done in the tracker, amend
   what changed, log the session, then run `git status` to confirm "done" means
   committed and pushed, not edited. No sitting closes with an unclean working
   tree unless the deviation is logged. (Fixed closing ritual — same status as
   Restart & Run All for notebooks.)

---

## Three living artifacts (keep in an appendix of the doc, or a companion "Article-notes" doc)

### A. Sources Ledger — every load-bearing claim maps to a source
| Claim (short) | Value in text | Source (full citation + URL) | Status | Last verified |
|---|---|---|---|---|
| latest Niño 3.4 (TONI) | +1.7 °C (wk of 17 Jun) | IRI Quick Look, Jun 2026 | CONFIRMED | 2026-07-07 |

### B. Hold List — facts pending, with a trigger
| Item | Current placeholder in text | Source to check | Trigger |
|---|---|---|---|
| very-strong probability | `[HELD: %]` | CPC ENSO Strength Probabilities (live) | July diagnostic ~9–10 |
| 97–98% NDJ persistence | `[HELD: confirm figure]` | IRI/CPC | July diagnostic ~9–10 |
| 1997/2015 analog magnitude | `[HELD: analog value at equiv. date]` | CPC ONI history | when Niño 3.4 pinned |
| "~1 °C warmer than 1997" | `[HELD: exact tropical warming]` | ERSST/OISST | with RONI number |

### C. Revision Log — the article's CHANGELOG
| Date | Session type | Section | What changed |
|---|---|---|---|
| 2026-07-07 | VERIFY | Intro | updated Niño 3.4 to +1.7 °C; added TONI/RONI hook; moved 4 items to Hold List |

---

## The "living document" rule (time-sensitive facts)

Some facts have a shelf-life — current Niño 3.4, forecast probabilities, grain stock-to-use ratios.
- Tag each in-text with an "as of \<date\>".
- Give the Sources Ledger row a **Last verified** date.
- Run a final **VERIFY-all** pass on every dated fact immediately before submission — none may be older than the latest monthly update.

---

## Priority order (from the article's own plan)

1. **Section 2 — Physical Science** (least developed; the foundation). Notebook-anchored: Bjerknes mechanics ← NB1; Southern-US flood signal ← NB2. *Draft with Claude.*
2. **Section 3 — CAT Modeling** (EP curves). Requires EM-DAT data acquisition + regression first.
3. **Sections 4–6** in sequence once 2 and 3 are done.

## Audience discipline

- **Primary = CAT modeling** — Sections 3–4 carry the hire signal; protect their rigor.
- **Secondary = PhD (transferable)** — do **not** distort the article toward coastal-megacity flood; its CAT integrity is the asset. The non-stationarity method, physical reasoning, and project execution *are* the PhD signal.

## Google Docs mechanics

- After each session, **name a version** in File → Version history (e.g., "2026-07-07 VERIFY Intro").
- Draft in **Suggesting mode**; accept a suggestion only once its `[verify]` is resolved.
- Keep the three artifacts (Ledger / Hold List / Log) in an appendix or a companion doc so they travel with the article.

## Between sessions / while holding

- Run **READ / COLLECT** sessions to pre-stage the Hold List's sources — so July 9–10 is a fast VERIFY, not a scramble.
- Read ahead for the *next* drafting target (Section 2) and populate the Sources Ledger with its citations, so drafting is assembly, not research.
- **Do not draft ahead of a scheduled co-draft session** — prep the ground; write together.

## Citation verification protocol
*Adopted 2026-07-14, after an audit found four of four sampled footnotes defective.*

### A citation is a premise. Own it.

**What the audit found:**
- **fn 6** — a fabricated title bolted onto a real, unrelated URL. The link pointed to the
  ECB *Environmental Statement 2025*, a report on the ECB's own carbon footprint, canteen
  waste and building emissions. The cited title did not exist. **Worse than the placeholder
  it replaced: silently broken, and it looked finished.**
- **fn 7** — correct authors, journal, volume, pages and year; **fabricated title and DOI.**
  That combination is the signature of a generated citation: correct scaffolding, invented
  identifiers. And on reading the real paper (Gaupp et al. 2020), it **contradicted the
  sentence it was supporting.** Dropped entirely.
- **fn 1** — source real, but it concerns **IAM damage functions**, while the sentence claimed
  **catastrophe models**. Category slippage: the exact error the target reader spots first.
- **fn 4** — a percentage **read off a plot**, attributed to the wrong product (the IRI
  model-based plume, not the CPC official forecast) on a stale access date.
- **Figure 2A** — a *different failure class*: the citation was correct (Solander's −0.07
  verified against Table 3) and **the figure was wrong** — it plots raw absolute soil
  moisture, so it renders climatology and was being read as drought, producing a caption
  that states the opposite of its own source.

### The migration pattern
The shortcut moves to wherever hasn't been defended yet:
1. Phase 1 reading questions → generated.
2. A 19-row results table → machine-transcribed.
3. **Article footnotes → generated.**

Each time, it appeared in the place the discipline had not yet reached. **Footnotes are the
worst of the three: they are the article's public epistemic surface.** A reader who clicks
one DOI, finds it fabricated, and stops reading — that ends the piece, and with it the very
claim to rigour the piece is making.

### The rule
- Every DOI resolves. Every URL opens to the thing it claims. Every title matches the page.
- Every number comes from a **table**, never a figure.
- Every citation supports **that sentence's** specific claim, not an adjacent one.
- **Read the paper.** Two of these defects were only visible from the full text.
- **Verifying the source is necessary and not sufficient.** Also verify that your own artifact
  computes what your prose says it computes.

### The through-line
Every failure in this project — the generated questions, the machine-transcribed table, the
fabricated footnotes, the figure cell written but never inserted, the raw-values map read as
an anomaly — is the same failure: **something entered an artifact without a witness.**
The fix is never a new tool. It is: *own the premise.*
