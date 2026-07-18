
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
