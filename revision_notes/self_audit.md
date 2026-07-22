# Self-audit — reconcile-pass commands with teeth

**Purpose.** Every check here inspects the *artifact itself* — the file's bytes, a cell's
execution count, the tracked-files list — never the memory of having done the thing. That is
the whole discipline of this project compressed into commands: a `grep -c` that returns `1`,
an `exec` count that isn't `null`, a `git status` that's clean. Each is a witness.

**When to run.** Group A every sitting-close. Groups B–D whenever a structural edit was made
(a checkbox ticked, a cell added, a block moved, a file staged).

**Recommended order within a sitting:**
- **At open:** run `audit.sh` (Group A + auto-generic parts of B–D). Cheap, generic, tells you
  whether the tree is honest before you touch anything.
- **During the sitting, right after each specific structural edit** (not saved up for later):
  go to Group B or C below, substitute today's real phrase / checkbox ID for the placeholder,
  and run that one command by hand.
- **Whenever `.gitignore` changes, or a file moves near an ignore boundary:** run Group D's
  `git check-ignore -v` spot-check on the moved/new path. This has no automated equivalent in
  `audit.sh` — it is easy to skip and easy to be wrong about without it.
- **At close:** run `audit.sh` again, then skim Commit discipline and Known artifacts below
  as a final check before pushing.

Run all from the repo root.

---

## A · Is the tree honest right now? (every sitting-close)

```bash
git status                          # clean? only intended untracked files (04_...ipynb)?
git --no-pager log --oneline -10    # do the messages match what I actually did?
git --no-pager diff --stat          # anything uncommitted I forgot? (the F.4 mixed-commit tell)
```
- `git status` should say "up to date with 'origin/main'" after a push, not "ahead by N."
- The only expected untracked file is `04_Ropelewski_Halpert_Atlas_Method.ipynb` (Q.6, intentional).

## B · Does a record match its artifact? (the "designed edits are not done" check)

```bash
# A ticked checkbox must correspond to a real thing:
grep -n "D.3\|B.3" revision_notes/task_B3_tracker.md

# A notebook cell claimed as "run" must actually have executed
# (exec=None everywhere means it was never run — the D.3 phantom-tick failure):
python3 -c "import json; nb=json.load(open('03_SEAsia_Drought_Data_Processing.ipynb')); print([c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code'])"

# A claimed edit must actually exist in the file (swap in a phrase from the edit):
grep -n "raw values, not anomalies" 03_SEAsia_Drought_Data_Processing.ipynb
```

## C · Orphans and duplicates (the bug that bit twice on 15 Jul)

```bash
# A block that should appear once: expect exactly 1. 2 = duplicate, 0 = missing/deleted.
grep -c "SOME_UNIQUE_PHRASE" revision_notes/task_B3_tracker.md

# Blocks that escaped their list item to column 0 (should return nothing):
grep -n "^RESOLUTIONS\|^[0-9]* Jul UPDATE" revision_notes/task_B3_tracker.md

# Numbered-item sanity (e.g. no accidental double-9):
grep -c "^9\. \|^10\. " revision_notes/task_B3_tracker.md
```

## D · Did anything unwanted get tracked?

```bash
git ls-files | grep -iE "synthetic|\.html$|_files/|\.nc$"   # should be empty
git check-ignore -v data/data_SYNTHETIC.nc                   # must print a rule
```

---

## Commit discipline (carry from the fault map)

- **One scope per commit.** Edit → commit → edit again. Never batch (F.4). The tell is a
  diffstat larger than the intended scope; `git --no-pager show --stat HEAD` after each commit
  should name only the files that scope touches.
- **A commit message is a premise.** Before writing "tracker: B.3 created", confirm B.3 exists
  (`grep -c "B.3"`). The message asserts a state; verify the state first.
- **Single-line `-m`.** Multi-line messages pasted into an active pager scramble the terminal.
- **`git rm` / `git mv`** for tracked files — Finder deletes are invisible to git.

## Known artifacts that travel with a fix (don't let the record drift)

- **Figure 2A PNG** (`figure_2A_SE_Asia_soil_moisture_OND1997.png`) is the raw-values map with
  the B.3 bug. When the anomaly is recomputed, **regenerate this PNG** or the repo keeps serving
  the wrong image under a corrected caption.

## What this audit CANNOT tell you

- It confirms **records match artifacts** (bookkeeping), not that the **science is right**.
- The **Google Doc article** is outside the repo — its footnotes and Figure 2A paragraph are
  not covered here. You are the witness on the Doc.
- Verified-by-assistant is not verified. Re-check every citation and number against its page.
