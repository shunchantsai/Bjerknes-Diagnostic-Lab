# Lessons — transferable rules, learned the hard way

*Reverse-chronological. Renamed from `git_and_data_ops_lessons.md` on 22 Jul 2026: the file
had long since outgrown that name — over half its entries are epistemics and workflow, not
git. **Test for entry: would this rule help on a different project, with different data?**
If it is specific to one source or one task, it belongs in the tracker or the session notes.*

## 24/07/26 — check which signal the skill is scoring

A forecast can be genuinely, verifiably skilful on the wrong variable — ASMC's
temperature panel scores well because it is detecting a warming trend against an
ageing 1991–2020 baseline, not because it has skill on ENSO. Skill on one panel
lends no credibility to the panel beside it. Related: agreement ≠ skill — shared
parameterisations and initialisation data produce consensus without independence,
so only hindcast verification (ROC) arbitrates. Same shape as the coherence/hit-rate
collapse: two statistics sitting at the same level of abstraction until separated.

## 23/07/26

- pip freeze is not a complete dependency witness in a conda environment — conda-installed packages carry no pip metadata and are silently absent. A pin file built from pip freeze alone can look complete while containing stale, unverified, or wrong entries for exactly those packages. Cross-check against conda list or the running kernel's own __version__ before trusting any pin.

## 22/07/26 — verification epistemics (from the RH87 literature session)

- **Matching digits are not a matching claim.** Searching for "0.80" surfaced "at least 80% of
episodes" and it was marked VERIFIED. But that 80% is a *hit rate* (a verification statistic);
the claim under test was a *coherence threshold* (a screening statistic). The premise turned out
true anyway — **which is worse**, because a correct conclusion from wrong evidence still carries
a VERIFIED tag downstream. Rule: state what a number should MEAN — formula, units, pipeline
stage — BEFORE going to look for it.

- **A verification that fails its own pre-registered expectation is not a closure.** An item
predicted "25 marked episodes, 20 below the median"; the count returned 12 and 11; it was marked
RESOLVED regardless, because the *direction* was right. The pre-registration exists to fire an
alarm on mismatch — do not let the desired conclusion overwrite it. If a count contradicts its
prediction, the item stays OPEN and **the discrepancy itself becomes the finding**.

- **A `[VERIFIED]` tag protects a claim from re-examination. That is its danger.** A quoted
figure was transcribed as "22 out of 25" next to a table reading 26, annotated "matches exactly."
It did not match, and it sat inside a verified block unread for nine days — because verified items
are precisely the ones you stop re-reading. Nine days later it corrupted a fresh count: I recounted
*expecting* 25, "found" 25, and nearly edited a correctly double-witnessed number down to match my
own typo. **Rule: when transcribing a quote containing a number, check it against the table in the
same motion. "Matches exactly" must be computed at the moment it is written, never asserted.**
**Corollary: a wrong number in notes is not inert — it does its damage later, by corrupting the
expectation you bring to the next measurement.**

- **Internal consistency is a form of verification.** Where a source is ambiguous, the resolution
tool is often the source's own other sentences: if reading A makes the paper's next claim false,
reading A is wrong. Used three times in one session. Formalised as the **three-witness rule** —
every number entering an artifact needs a second independent witness in the source.

- **An artifact can be internally consistent and still wrong.** A table satisfying its own
arithmetic (`wet + dry = total`) still disagreed with the prose and figure it summarised. An
internal-consistency check is necessary, **not sufficient**. → A pipeline that *prints* its
intermediate counts makes this visible; one that merely balances them does not.

- **A figure is immune to typesetting error, not to reading error.** Bar charts were adopted as
the strongest witness because "a bar chart cannot be mis-typeset" — true, and it misled. Bars near
the median are near-zero length and unresolvable at scan resolution. **A figure is a strong witness
for SENSE and SEASON, a weak one for TOTALS.** Where a table and prose agree verbatim, a discordant
bar count is evidence about your counting.

- **An assistant's claims about what a source says are hypotheses, not findings.** Tally over one
session: source-content claims 0 for 5; derivations from stated premises, correct every time
checked. Use the reasoning; verify every assertion about the page.

*(Not repeated here: one-scope-per-commit and `git mv`/`git rm` — already in `self_audit.md`
§Commit discipline and in the 10/07/26 entry below. The "shortcut migrates" pattern lives in
`Article_Writing_Workflow.md` §The migration pattern.)*

## 20/07/26

- An empty stage is silent. `git commit` with nothing staged prints a status block and exits 0
— no error, no commit. Chaining `git diff --staged --stat && git commit` does NOT catch it,
because git diff exits 0 whether or not a diff exists. Three commits in one session were lost
this way and only surfaced at the closing audit. Use `git status --short` before committing: it
prints NOTHING when nothing is staged (unmissable) and M/A lines when there is.

- Staged text applied before its gate creates the defect the staging existed to prevent. The
Fig 2A anomaly caption was written in advance, marked "do not apply until the anomaly figure
exists", then pasted into the Doc over the OLD absolute-values figure — where it sat for a day
asserting an anomaly that had not been computed. Same failure class as ticking an undone task,
arriving from the opposite direction: not a record ahead of the artifact, but prose ahead of it.
Fix that worked: the gate travels INSIDE the staged text, and the staged block is marked
SUPERSEDED the moment real text ships, so no future reader can re-apply a pre-computation draft.
Corollary: a figure and its caption are one artifact — swap both or neither.

## 18/07/26

- GES DISC / curl -LJO: a failed request (e.g. 401) has no Content-Disposition header,
so -J falls back to the URL's last path segment — the file saves as HTTP_services.cgi,
not under the expected LABEL name. Batch failures therefore accumulate as
HTTP_services.cgi.N rather than as missing data filenames. Always verify a batch by
BOTH counting expected .nc4 files AND confirming zero HTTP_services.cgi* exist.
Magic-byte check (`file`) distinguishes the 401 page from real netCDF.

- curl -J refuses to OVERWRITE an existing local file: it aborts with
"curl: (23) client returned ERROR on write" and leaves the stale copy in place.
A re-pull into a populated directory therefore keeps old files silently while the
file COUNT still verifies correct. Count alone is not sufficient — check mtimes
(`ls -lh`) so stale files can't hide inside an otherwise-correct batch. Fix: delete
the offenders and re-fetch only those URLs.


## 17/07/26

— Footnote references rot. Inserting/deleting a footnote renumbers everything
after it, silently invalidating every numeric fn reference in the tracker. Locate
footnotes by CLAIM CONTENT, never by arithmetic: the "obvious" −1 shift was predicted,
applied, and disproven the same day. Rule: tracker records claim text + number; re-run
the content mapping after ANY fn insertion or deletion.

— Claude's bookkeeping assertions are not sources either. A predicted fn
mapping was pasted into the tracker as if verified; the Doc check showed it wrong. The
epistemic standard applies to metadata (numbers, filenames, dates) exactly as to
scientific claims.

— Live URLs that host superseded issuances (CPC ensodisc.shtml) make "accessed
<date>" ambiguous: the date may postdate the cited issuance. Archive a PDF at read time
and cite issuance date + archive note. Corollary caught today: publication date ≠ access
date — a citation claiming "accessed 19 June" for a page updated 3 July is self-refuting.

— Unlike quantities compared unlabeled: "+0.94 in May" (monthly, two decimals,
ERSSTv5-style) vs "+1.7 wk of 17 Jun" (weekly, one decimal). Decimal precision is a
provenance fingerprint — a two-decimal value cannot come from the one-decimal weekly file.
Label the basis of every number in a comparison.

— Existence claims about files get checked with ls, same as everything else:
yesterday's closing note denied self_audit.md existed; the repo contained it (5b0f915).

— When a source doesn't state your claim at your claim's scope (Ch.2: global
SST only, not tropical), check the sibling chapter before weakening the wording: Ch.9
§9.2.1.1 carried "tropical" cleanly. Document negative reads — they're reusable.

## 15/07/26 — decouple the deliverable from the blocked dependency

When NB3's data access stalled with no ETA, the reflex was "wait for approval." Better:
ask what the deliverable actually depends on. The article's CLAIMS rest on RH87 base
rates + mechanism (in hand); the IRI forecast fills one section whose FRAMING (live
forecast vs. retrospective validation) depends on timing, but whose PLACE in the article
is fixed. Reframing made the article licence-independent — the blocker sets the tense of
one paragraph, not the critical path. Rule: when blocked, separate what the work needs
from what it merely wants; a dependency with no ETA should be made a drop-in, not a gate.

## 15/07/26 — a "done" edit is a claim; verify the artifact, not the record

Across one commit session, five edits recorded as done pointed at the wrong file,
wrong path, wrong cell, or nothing: (1) the notebook staged was the pre-rebuild
version; (2) build artifacts (.html/_files) were about to be committed; (3) the
lessons file was untracked and at a different path than assumed; (4) the 14 Jul
lesson was deleted from CHANGELOG but never written to the lessons file; (5) a
tracker block was duplicated, not moved. Every one was caught by a grep or a
Restart-and-Run-All BEFORE it committed. Rule: after any edit, run a witness that
inspects the artifact itself (grep -c, git diff --stat, show --stat, a full run) —
never trust the memory of having made the change. A commit message is a premise.


## 14/07/26 — a diagnosis that explains the symptom is not necessarily the cause

On 10 Jul, urllib/curl against IRIDL returned HTML instead of NetCDF. Diagnosis:
the dlauth login gate. That fully explained the symptom, so it looked confirmed,
and the workflow was rebuilt around it ("download logged-in in the browser"). It
was incomplete — behind the login gate sat a LICENCE gate (protected domain
iri.columbia.edu/terms/forecast/1). Confirmed 14 Jul only by testing the download
end-to-end while fully authenticated: redirected to /auth/credential?...&realm=
iri.columbia.edu/terms/forecast/1. Being logged in was never sufficient.
- A hypothesis that accounts for the symptom is one candidate cause, not THE cause.
- Test the whole path; don't reason about it. Four days of workflow were built
  around a gate that wasn't the binding one, because the binding one was never probed.
- Corollary: the same failure produced a phantom ref id. f8725d… sits in the tracker
  with no confirmation email in any inbox — a single-source, unverifiable claim.

## 14/07/26 — designed edits are not done edits (3rd occurrence)

NB3's four-panel figure cell was "written 10 Jul" — in the session NOTES, never
inserted into the notebook. Tracker D.3 was ticked [x]. In reality cells 19-20 were
comment placeholders, and there was no extraction cell and no GRID CHECK cell: half
the pipeline did not exist, so the dry run would have failed even with valid data.
The reconcile pass must OPEN THE ARTIFACT, not just the record of the artifact.
(1st: 11 Jul, download cell never applied. 2nd: D.3 phantom tick. This is the 3rd.)

## 11/07/26 — commit messages describe the diff, not the day

Follow-up commit (980d4a6) reused the previous commit's message verbatim —
message describes the wrong changes. Rule: write the message after
`git diff --staged`, describing what's actually staged; if the follow-up
lands within minutes and nothing was pushed yet, `git commit --amend` instead.

## 10/07/26 (git, files, notebooks, terminal)

1. Git only knows what's committed. git log --since returning nothing meant three days of work existed only in the working tree — invisible to history, to GitHub, and to any backup. Corollary: the template→NB3 "rename" was never a rename to git, because the original was never committed; it entered history as a plain add. The changelog must describe what the repository saw, not what happened on disk.
2. Untracked files accumulate silently and need triage, not bulk-add. One git status revealed five distinct categories mixed together: deliverables that should have been committed long ago (LICENSE, Figure 2A), data inputs that must never be committed (GLDAS .nc4), provenance recipes worth keeping in a named folder (data_provenance/), third-party material that can't legally be redistributed from a public repo (references/ — bulletins, snapshots), and junk (HTTP_services.cgi). Each category gets a different verb: commit, ignore, relocate-and-commit, ignore-with-backup, delete.
3. Never assume .gitignore — verify it. I believed data/ was ignored; git check-ignore -v <file> proved it wasn't (empty output = not ignored; otherwise it names the exact rule and line). That one command replaces guessing.
4. Ignored ≠ backed up. Git protects only what it tracks. references/ being ignored means git will never save it — so it needs its own backup path (iCloud sync counts for hardware failure, but sync propagates deletions; it is not versioned history).
5. Moving files and editing the code that reads them is one atomic change. Relocating the GLDAS inputs to data/ broke NB3's Task 2A paths until the three open_dataset calls were updated — so the move and the path edits belong in the same commit, verified together by running the affected cells before committing.
6. One scope per commit; commit ≠ changelog. Eleven single-scope commits made today's history legible line by line. The granularity rule underneath: every repo change gets a commit; only changes notable to an outside reader get a CHANGELOG entry. The changelog says what changed in a screenful; the revision note says how the session went.
7. Push is the off-site half of the system. Being "10 commits ahead of origin" meant the entire portfolio existed on one laptop. Commit ends a task; push ends the day.
8. Notebooks lie in two specific ways. (a) Duplicate cells run without error when the operations are idempotent — the 2A fossil cell recomputed identical values silently; "it works" is not "it's right." (b) Execution order is top-to-bottom, so a stale config cell below a new one wins — configuration must have exactly one home. Also: filenames must not lie (_DRYRUN in the name because June data is throwaway).
9. Terminal diagnostics beat guessing. ls -lh (a 4.4K "dataset" is not a dataset), head -c 500 (revealed the dlauth login page masquerading as .nc), magic bytes (CDF/HDF = NetCDF, <!DO = HTML). And a download cell guarded by if not raw.exists() caches its own failures — delete the bad file before retrying, and build the magic-byte assert into the cell so the failure mode can never pass silently again.
10. The dry run is where assumptions die cheaply. One rehearsal on June data surfaced the auth gate, the license-approval gate, and the L-axis season ceiling — five days before they'd have detonated on issuance day. Rehearse the pipeline before the day the output matters.
11. Documents drift from reality unless reconciled ritually. Tracker seasons vs. notebook seasons, ticked boxes vs. actual notebook state, changelog vs. git log — every problem found today was the same problem. The fix is a fixed two-minute closing pass: tick what's done, amend what changed, log the session, commit, push. And stray notes are deleted only after checking every claim in them is done or carried by the tracker.
