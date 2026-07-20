# revision_notes/ — what each file is for

Process documentation for the Bjerknes Diagnostic Lab. The repo root holds things an
outside reader consumes (notebooks, modules, tests, README, CHANGELOG, TODO); this
folder holds everything about *how the work is done*.

If you are unsure where something goes, use the decision rule at the bottom.

---

## The seven files

### `../TODO.md` (repo root)
**What:** the plan. The only place tasks are ordered and picked.
**Write when:** every sitting — open (pick 1–3 into NOW) and close (tick, or annotate
"blocked because X"). Discoveries mid-session get ONE line in NEXT or WAITING.
**Never:** reasoning, evidence, or history. One or two lines per item, with a pointer
into the tracker for detail. A completed item leaves TODO only once its record exists
in the CHANGELOG or the tracker — never delete a task whose only trace was here.
**Structure:** WARNINGS (standing hazards, not tasks) · NOW · NEXT (ordered) ·
WAITING (gated, trigger named) · RECURRING · PARKED.

### `task_B3_tracker.md`
**What:** task state and evidence. Per-task diagnosis, closed facts with quoted
sources, staged text, standing decisions, gates.
**Write when:** a task changes state, or a verification closes. Every closure gets an
evidence line: what was checked, against which source, on what date.
**Never:** the queue (that is TODO's job — two queues drift and contradict).
**Test of a good entry:** a reviewer could re-walk your verification from it alone.

### `article_ledger.md`
**What:** the three living artifacts for the article —
**A. Sources Ledger** (every load-bearing claim → its source, with a Last-verified date),
**B. Hold List** (facts pending, each with a trigger),
**C. Revision Log** (the article's own changelog: date, session type, section, what changed).
**Write when:** after any session that touches the Google Doc.
**Note:** the Doc's appendix holds a *mirror* so the artifacts travel with the article.
Edit here first, then regenerate the mirror.

### `git_and_data_ops_lessons.md`
**What:** transferable rules learned the hard way. Reverse-chronological, dated.
**Write when:** something went wrong in a way that will recur.
**Test:** would this rule help on a different project, with different data? If it is
specific to one source or one task, it belongs in the tracker instead.
**Example that belongs here:** "curl -J refuses to overwrite; a re-pull silently keeps
stale files while the file count still verifies correct."
**Example that does not:** "Solander Table 3 is unit-silent" — that is one source, so
it is a tracker entry.

### `Article_Writing_Workflow.md`
**What:** protocol for writing the article — the five disciplines, the session types
(READ/COLLECT · DRAFT · VERIFY · RESTRUCTURE), the per-session loop, the citation
verification protocol.
**Write when:** a protocol changes. This file should be nearly static.
**Never:** task state, or the three artifacts (they live in `article_ledger.md`).

### `sessions/<date>_<arc>_notes.md`
**What:** one file per **arc** — a unit of work with a finish line (a lit session on one
paper, a notebook deep-read phase, a build). The filename carries the arc's START date
and never changes; each sitting appends a dated entry inside.
**Write when:** the notes *are* the deliverable — reading, comprehension, design.
Ops and verify sittings log to TODO + tracker + CHANGELOG instead and produce no notes file.
**Rules:** multiple arcs may be open at once (cap: two — one critical-path, one study).
The one-scope discipline is per *sitting*, not per day or per file. When an arc's exam
and fault map are done, add `CLOSED <date>` at the top and never edit it again.

### `audit.sh` and `self_audit.md`
**What:** the reconcile pass, as an executable and as its rationale.
**Run when:** at sitting open and at sitting close — `bash revision_notes/audit.sh`.
**Reads:** tree honesty (git status, recent commits, uncommitted diffstat), notebook
execution counts, tracker orphans, unwanted tracked files, untracked files, and the
head of TODO.md. Paste the output into the chat to sync state.

### `../CHANGELOG.md` (repo root)
**What:** repo changes notable to an *outside reader*, in a screenful.
**Write when:** a session produced something a stranger reading the repo would care about.
**Never:** every commit. Commits are granular; the CHANGELOG is editorial.
Rule of thumb: every repo change gets a commit; only notable ones get an entry.

---

## The daily loop

**OPEN (5 min):** run `audit.sh` → read TODO's NOW → move 1–3 items in → declare the
session type (one scope: content, structural, ops, verify, reading).

**WORK:** only NOW items. Anything discovered gets one line in NEXT/WAITING and is not
acted on. Chat is not a document — anything decided in conversation that matters gets
written into TODO or the tracker before the sitting ends.

**CLOSE (10 min):** tick/annotate TODO → evidence lines into the tracker → lessons and
CHANGELOG if earned → `git add` → `git status --short` (prints nothing if nothing is
staged) → single-scope commit → push → `audit.sh` → paste output.

---

## Decision rule — where does this go?

| The thing you have | Goes in |
|---|---|
| A task to do | TODO.md |
| Why a task is deferred, and what "done" requires | tracker (+ one pointer line in TODO) |
| A verification you completed | tracker, with the source quoted |
| A claim now in the article, and its source | article_ledger.md § A |
| A fact you cannot verify yet | article_ledger.md § B, with a trigger |
| A change you made to the Doc | article_ledger.md § C |
| A rule that will help on a future project | lessons file |
| A change an outside reader should know about | CHANGELOG.md |
| A change to how you work | Article_Writing_Workflow.md |
| Reading notes, comprehension, design thinking | sessions/<arc>.md |

**Two standing rules that override everything:**

1. *Designed edits are not done edits.* "Done" means committed and pushed, confirmed by
   `git status` and `git log` — not edited, not intended, not described in chat.
2. *Own the premise.* Nothing enters an artifact without a witness. Every number comes
   from a table or your own computation; every citation is opened and read; every
   "already done" is checked with `grep`, `ls`, or a full run. Claude's assertions are
   not a source — including its assertions about your own files.
