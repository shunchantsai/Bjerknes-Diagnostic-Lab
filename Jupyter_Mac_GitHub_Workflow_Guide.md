# Jupyter → Mac → GitHub: The Complete Workflow

## A practical guide based on real mistakes made while building the Bjerknes Diagnostic Lab project.

---

## The Three Layers

There are three places your files can live, and they are **independent** of each other:

```
┌─────────────────────┐
│  1. JUPYTER MEMORY   │  ← What Python is running right now (lost on kernel restart)
└─────────┬───────────┘
          │ Saving the notebook writes the .ipynb to disk
          │ But does NOT update any .py files
          ▼
┌─────────────────────┐
│  2. FILES ON DISK    │  ← What Finder shows you in your project folder
│     (your Mac)       │     .ipynb and .py are separate files here
└─────────┬───────────┘
          │ git add + git commit + git push
          │ Only staged/committed changes go to GitHub
          ▼
┌─────────────────────┐
│  3. GITHUB           │  ← What the world sees at github.com/you/repo
└─────────────────────┘
```

**The critical rule:** Changes only flow downward through explicit actions. Nothing is automatic. Saving a notebook does not update a `.py` file. Editing a `.py` file does not push to GitHub. You must move changes through each layer yourself.

---

## The Daily Workflow

### Step 1: Always launch Jupyter from inside the cloned repo

```bash
cd /Users/dantsai/Documents/GitHub/Bjerknes-Diagnostic-Lab
jupyter notebook
```

This ensures every file you edit is the git-tracked copy. If you launch Jupyter from a different folder, you'll create or edit files that git doesn't know about.

### Step 2: Edit your notebook and/or .py files

Work normally in the notebook. When you're done, **save the notebook** (Cmd+S or File → Save).

### Step 3: Open a second terminal for git

Don't close the Jupyter terminal (that kills your notebook server). Open a new Terminal window (Cmd+N) or tab (Cmd+T), then:

```bash
cd /Users/dantsai/Documents/GitHub/Bjerknes-Diagnostic-Lab
git status          # see what changed
git add <files>     # stage specific files (or git add . for everything)
git commit -m "Descriptive message about what you changed"
git push origin main
```

---

## The Pitfalls (All Encountered in This Project)

### Pitfall 1: Defining functions in notebook cells instead of the .py file

**What happened:** You built `plot_scenario`, `lon_fmt`, `DEFAULT_X`, and the improved `find_zero_crossings` inside notebook cells. They ran perfectly. But `bjerknes_physics.py` on disk still contained only the original 25-line version.

**Why it's confusing:** Everything works in Jupyter because Python loaded the functions into memory from the cells. You can even `import bjerknes_physics` and then redefine a function in a later cell — the cell definition wins, and nothing seems wrong.

**The rule:** A `.ipynb` file and a `.py` file are separate documents. Saving the notebook never updates the `.py` file. They don't know about each other.

**The fix:** Use `%%writefile` to write a cell's contents to a `.py` file on disk:

```python
%%writefile bjerknes_physics.py
# entire file contents go here — the first line MUST be %%writefile
import numpy as np
def pressure(x, A, x0, w, base):
    ...
```

The `%%writefile` command and the code must be in the **same cell**. An empty cell with just `%%writefile filename.py` will error.

---

### Pitfall 2: Old function definitions lingering in memory

**What happened:** You fixed `plot_bjerknes_diagnostic` to use `axes.ravel()`, but Jupyter kept calling the old version that used bare `ax.plot()`. Restarting the kernel didn't help.

**Why it's confusing:** If the cell that defines the function still contains the old code, restarting the kernel and re-running all cells just reloads the bug.

**The rule:** The kernel restart clears memory, but then re-runs whatever is in the cells. If the buggy definition is still sitting in a cell, it gets reloaded.

**The fix:** Find the cell with the old definition (use Cmd+F to search for the function name). You may have duplicate cells defining the same function — delete the old one, keep only the corrected one. Then Kernel → Restart & Run All.

---

### Pitfall 3: Mismatched parameter names between function signature and body

**What happened:** The function signature said `title=""` but the body used `scenario_title` and `subtitle`, causing `NameError: name 'scenario_title' is not defined`.

**Why it's confusing:** You copied code from one function (`plot_scenario`) into another (`plot_bjerknes_diagnostic`) without updating the parameter names.

**The rule:** If the function body uses a variable name, that name must either be a parameter in the signature, defined inside the function, or a global. Python doesn't guess that `title` and `scenario_title` are meant to be the same thing.

**The fix:** Make sure every variable in the body matches a parameter name or is defined locally. When copying code between functions, always check the signature.

---

### Pitfall 4: Undefined colour constants

**What happened:** The plotting code referenced `C_PT`, `C_PTD`, `C_DP`, `C_GRAD` but these were never defined in the notebook.

**Why it's confusing:** These were defined in the standalone `.py` file you were given, but when you copied only the plotting function into a notebook cell, you didn't bring the constants along.

**The rule:** When you copy a function from one context to another, you must also bring all its dependencies (imports, constants, helper functions).

**The fix:** Define the constants before the function that uses them, or import them from the `.py` module.

---

### Pitfall 5: `git diff` shows nothing, but GitHub has old code

**What happened:** You ran `git diff bjerknes_physics.py` and it showed no changes. But GitHub still had the old 25-line version.

**Why it's confusing:** `git diff` compares the file on disk to the last commit. If the file on disk was never changed (because you were defining functions in notebook cells, not editing the `.py` file), the diff is genuinely empty — there's nothing wrong with git, the file really is unchanged.

**The rule:** `git diff` compares disk vs. last commit. If the file on disk is the old version, and the last commit is also the old version, git correctly reports no difference.

**The fix:** This is Pitfall 1 in disguise. You need to actually write the updated code to the `.py` file on disk (via `%%writefile`, a text editor, or any other method), then `git add`, `commit`, `push`.

---

### Pitfall 6: Finder shows a recent modification date but the file contents haven't changed

**What happened:** Finder showed both files as recently modified, so you assumed the contents were updated.

**Why it's confusing:** Jupyter touches files in the project directory (metadata, checkpoints) even without changing the actual code. The modification timestamp updates, but the file contents may be identical to before.

**The rule:** Modification dates tell you when the file was last written to, not whether the content changed. Only `git diff` or actually reading the file tells you what's inside.

---

### Pitfall 7: `%%writefile` with an empty cell body

**What happened:** You put `%%writefile bjerknes_physics.py` in a cell by itself and ran it, getting `UsageError: %%writefile is a cell magic, but the cell body is empty`.

**Why it's confusing:** It looks like a command you'd run on its own line.

**The rule:** `%%writefile` is a cell magic — it acts on the entire cell body. The first line is the command, everything below it (in the same cell) is what gets written to the file.

**The fix:** Put the magic command on line 1 and the full file contents below it, all in one cell.

---

### Pitfall 8: The `axes.ravel()` unpacking for `plt.subplots(2,2)`

**What happened:** `fig, ax = plt.subplots(2, 2)` returns `ax` as a 2×2 numpy array. Calling `ax.plot()` fails with `AttributeError: 'numpy.ndarray' object has no attribute 'plot'`.

**Why it's confusing:** `plt.subplots()` with a single panel returns a single Axes object (so `ax.plot()` works). With multiple panels it returns an array (so it doesn't). The API behaves differently depending on the arguments.

**The rule:** Always unpack multi-panel subplots explicitly:

```python
fig, axes = plt.subplots(2, 2)
ax1, ax2, ax3, ax4 = axes.ravel()   # four individual Axes objects
```

---

### Pitfall 9: `np.where()` returns a tuple

**What happened:** `find_zero_crossings` looped over `np.where(np.diff(s) != 0)` without `[0]`, iterating the tuple once instead of over the indices.

**The rule:** `np.where(condition)` returns a **tuple** of arrays (one per dimension). For a 1D array, you need `np.where(condition)[0]` to get the actual index array.

---

## The Sync Layer: When Local and GitHub Disagree

The Pitfalls above are all about the **Jupyter ↔ disk ↔ .py** boundary. This section is about the **disk ↔ GitHub** boundary — what happens when your local repo and the GitHub remote have *diverged* (each has commits the other lacks). This is a completely different class of problem, and it shows up the moment you've edited on GitHub's website AND locally, or pushed from two machines, or — as happened here — committed locally while the remote moved ahead.

### The mental model: history is a chain, not a folder

GitHub doesn't just store your *current files* — it stores the entire **chain of commits** that produced them. Two ideas follow from this, and they cause most of the confusion:

1. **"Current view" vs. "history" are different.** A file you deleted in a recent commit is gone from the current view but still **recoverable from history** (an older commit still contains it). Deleting a file does not erase its past.
2. **Local and remote are two separate chains** that are supposed to stay in sync. When they diverge, git refuses to push until you reconcile them — this is a safety feature, not a bug.

---

### Pitfall 10: "Updates were rejected (fetch first)" — the remote moved without you

**What happened:** `git push` was rejected with *"Updates were rejected because the remote contains work that you do not have locally."*

**Why it's confusing:** You committed locally and expected to push cleanly. But someone — often **you, editing a file directly on github.com and forgetting** — added a commit to the remote that your local copy never saw.

**The rule:** Git won't let you push if the remote has commits you don't have, because doing so could erase that remote work. The two chains have diverged and must be reconciled first.

**The fix — see what diverged before reconciling:**
```bash
git fetch origin                    # download remote state WITHOUT merging
git log --oneline origin/main -5    # last 5 commits on GitHub
git log --oneline main -5           # last 5 commits locally
```
Compare the two logs. Find the commit where they split — everything above it differs. Now you know exactly what's on each side before you touch anything.

---

### Pitfall 11: `git pull` vs `git pull --rebase` — don't make a tangled merge

**What happened:** After a rejected push, the hint says "use git pull." A plain `git pull` would create a **merge commit** that ties the two chains together with an ugly fork in the history.

**Why it's confusing:** Plain `git pull` works, but on a diverged history it produces a messy non-linear log (a visible fork-and-rejoin), and it can auto-merge files in ways you didn't review.

**The rule:** `git pull` = fetch + **merge** (creates a merge commit). `git pull --rebase` = fetch + **replay your commits on top** of the remote's (keeps history linear, no merge commit). For a personal repo, rebase is almost always cleaner.

**The fix — always rebase, and back up first:**
```bash
git branch backup-before-rebase     # safety bookmark — if anything breaks, you can return
git pull --rebase origin main       # replay your local commits on top of the remote's
```
If the rebase goes wrong at any point: `git rebase --abort` returns you to exactly where you started. The backup branch is a second safety net.

---

### Pitfall 12: A rebase stops on a CONFLICT — and `--theirs`/`--ours` are reversed

**What happened:** During the rebase, git stopped with *"CONFLICT (content): Merge conflict in README.md"* because both your local commit and the remote commit edited the same file.

**Why it's confusing:** A conflict feels like an error, but it's just git asking you to choose, because it can't auto-merge two different edits to the same lines. **And the `--theirs`/`--ours` labels are backwards during a rebase** compared to a normal merge.

**The rule:** During a **rebase**, `--theirs` means *your* incoming commit's version, and `--ours` means the remote base you're replaying onto. (Yes, this is the opposite of intuition — it trips up everyone, because rebase replays your work *onto* the remote, so from git's internal seat the remote is "ours.")

**The fix — keep your version of the conflicted file:**
```bash
git checkout --theirs README.md     # keep YOUR version (during rebase, --theirs = yours)
git add README.md                   # mark the conflict resolved
git rebase --continue               # proceed
```
If unsure which is which, open the file in a text editor *before* `git add` and read it — don't trust the flag name blind. If the rebase completes with no conflict at all, it'll say *"Successfully rebased and updated"* — in that case there is nothing to resolve; do not run the conflict commands.

---

### Pitfall 13: Untracking a file vs. deleting it (and why `.gitignore` isn't enough)

**What happened:** You wanted a PDF *kept on your Mac* but *removed from GitHub*. Adding it to `.gitignore` did nothing, because the file was already tracked.

**Why it's confusing:** `.gitignore` only stops git from tracking files it isn't *already* tracking. A file that's already committed keeps being tracked regardless of `.gitignore`.

**The rule:** Three different operations, three different outcomes:
- `git rm file` — deletes from git **and** from your disk.
- `git rm --cached file` — **untracks** from git but **keeps the file on your disk**. This is what you want for "stop publishing it, but I still want my copy."
- adding to `.gitignore` — only prevents *future* tracking of not-yet-tracked files.

**The fix — untrack but keep on disk:**
```bash
git rm --cached "filename.pdf"      # untrack, but file stays on your Mac
echo "*.pdf" >> .gitignore          # prevent re-tracking any PDF in future
git add .gitignore
git commit -m "Untrack PDF, keep locally"
```

---

### Pitfall 14: "Untracked file would be overwritten" during a rebase/merge

**What happened:** The rebase aborted with *"The following untracked working tree files would be overwritten: Github 5_ El Nino.pdf — Please move or remove them."*

**Why it's confusing:** A file sitting **untracked on your disk** has the same name as a file that one of the replayed commits tries to *add*. Git won't clobber your untracked copy, so it stops.

**The rule:** Git protects untracked files from being silently overwritten by an incoming commit. If a commit being replayed adds a file you currently have as untracked, you must clear the collision first.

**The fix — back it up, move it out, then proceed:**
```bash
cp "Github 5_ El Nino.pdf" ~/Desktop/BACKUP.pdf   # safety copy FIRST (especially for unfinished work)
mv "Github 5_ El Nino.pdf" ~/Desktop/working.pdf  # move it out of the repo folder
git pull --rebase origin main                     # now the rebase can replay cleanly
# ...after the rebase finishes and the file is untracked/ignored:
mv ~/Desktop/working.pdf "Github 5_ El Nino.pdf"  # move it back; .gitignore keeps it untracked
```

---

### Pitfall 15: Renaming a notebook while Jupyter still has it open

**What happened:** After `git mv notebook.ipynb 01_notebook.ipynb`, the **old filename reappeared** on disk as an untracked file, threatening to leave duplicate notebooks in the repo.

**Why it's confusing:** `git mv` renamed the file, but Jupyter still had the notebook open under the *old* path. Its next autosave wrote the old-named file back to disk.

**The rule:** Renaming a file out from under a program that has it open invites that program to recreate the old name. Jupyter autosaves to whatever path it opened.

**The fix:** **Close the notebook in Jupyter (shut the kernel) before renaming.** If the old name reappears, first confirm it's a true duplicate, then delete it:
```bash
git diff --no-index "old_taskname.ipynb" "01_new_name.ipynb"   # empty output = identical duplicate
rm "old_name.ipynb"                                        # plain rm (it's untracked); safe if diff was empty
```
If the diff shows *differences*, the old-named copy has newer edits — move that content into the renamed file before deleting.

---

### Pitfall 16: Committing notebook outputs (the invisible token tax)

**What happened:** Every time you re-ran the Bjerknes notebook and committed, the `.ipynb` grew and `git diff` showed thousands of changed lines you never typed. Later, when the repo was synced into a Claude Project, the notebook ate far more of the context budget than its ~200 lines of code should have.

**Why it's confusing:** A `.ipynb` is JSON, and it stores cell **outputs** inline — including every matplotlib figure as a base64-encoded PNG blob. Your three-panel plots become tens of thousands of characters of gibberish text living inside the file. The code is maybe 5% of the file's weight; the embedded images are the rest.

**The rule:** Re-running a cell changes its output blob, so git sees the file as changed even when the code is identical. Those blobs bloat the repo, make diffs unreadable (giant base64 walls), and inflate the token cost every time a tool — Claude included — has to read the notebook.

**The fix — strip outputs before committing:**
```bash
# one-off, in place:
jupyter nbconvert --clear-output --inplace 01_Bjerknes_Zonal_Diagnostic.ipynb

# or automate it forever with a git filter (recommended):
pip install nbstripout
nbstripout --install        # run once inside the repo; strips outputs on every commit automatically
```
After this, the committed notebook carries only code + markdown. Diffs show the lines you actually changed, and the file's token weight drops to roughly its code weight. Your plots still render live in Jupyter — you're only stripping the *saved* copy, not what's in memory.

---

## Layer 4: Tokens & the Claude Project Sync

The three layers above end at GitHub. But there's a fourth place your files travel to: a **Claude Project**, when you connect the repo as project knowledge. This layer has its own rules, and they're about *tokens* — how much of Claude's context budget your files consume.

```
┌─────────────────────┐
│  3. GITHUB           │
└─────────┬───────────┘
          │ "Sync now" fetches the current file contents from the branch
          │ (names + contents only — no commit history, PRs, or metadata)
          ▼
┌─────────────────────┐
│  4. CLAUDE PROJECT   │  ← What Claude reads as project knowledge
│                      │     Updated ONLY when you click "Sync now"
└─────────────────────┘
```

**The critical rule (same spirit as Layer 1–3):** the sync is not automatic. The Project holds whatever was on the branch at the last "Sync now." Push all you like — Claude won't see it until you sync.

### How the sync actually costs tokens

Three facts that fix the usual misconceptions:

1. **Sync re-loads whole files, not your diff.** When you push 5 edits and click "Sync now," the Project doesn't ingest "5 changes" — it re-fetches the **entire** files that changed. The cost of a sync is set by the *size of the file*, not the size of your edit. A one-line change to a bloated notebook re-ingests the bloated notebook.

2. **Within one conversation, synced files are cached.** Claude caches project knowledge, so only new/uncached content counts against usage. Reading the notebook in turn 1 and referencing it again in turn 8 of the *same* chat is cheap — you are not paying full price every message.

3. **`.ipynb` size is dominated by outputs, not code** (see Pitfall 16). An unstripped notebook can cost 10–50× its code weight in tokens. This is the single biggest lever on sync cost.

### Sync vs. paste: which to use

**Paste just the change (cheapest).** For a focused "review this one function" question, paste the `git diff` output — not two full copies of the file. A unified diff shows only the changed lines plus a little context, so it beats old-version-plus-new-version on tokens and is easier to read. You skip the entire notebook JSON.
```bash
git diff bjerknes_physics.py            # unstaged edits
git diff HEAD~1 bjerknes_physics.py     # vs. the previous commit
```

**Keep the Project sync (whole-project context).** Worth it when Claude needs to reason across the *whole* repo — "does this change to the classifier break anything in notebook 02?" The cost is that the full files sit in knowledge, so those files must be lean (strip outputs, keep logic in `.py`).

**Never do both at once.** A bloated synced repo *plus* pasting big chunks double-loads the same content.

### Recommended workflow

- **Keep the physics in `.py`, notebook as a thin driver.** (This is Pitfall 1 paying off again.) `bjerknes_physics.py` holds the logic as pure text — tiny, clean diffs, cheap to read. The notebook just imports and plots. Point Claude at the `.py` file for logic review.
- **Strip notebook outputs** (Pitfall 16). Lean notebooks = cheap syncs *and* readable diffs.
- **For focused edits (most of the time):** paste `git diff` in a normal chat. Fast, cheap, targeted.
- **For "reason across my whole repo" sessions:** use the Project sync — but sync *deliberately*, after a meaningful batch of changes, not reflexively after every push.
- **Refresh before analysis.** The Project holds whatever was there at the last sync. Hit "Sync now" at the start of any session where currency matters — the same instinct as `git fetch` before reconciling (see The Sync Layer).

---

## Q&A

**Q: I edited my notebook and saved it. Is `bjerknes_physics.py` also updated?**
A: No. They are separate files. Saving the notebook only updates the `.ipynb` file. To update the `.py` file, either use `%%writefile` from within the notebook, or edit the `.py` file directly in a text editor.

**Q: I defined a function in a notebook cell AND it exists in the .py file. Which one does Python use?**
A: Whichever was executed **last**. If you `import bjerknes_physics` in cell 3 and then redefine `find_zero_crossings` in cell 7, cell 7's version wins from that point forward. This is a common source of confusion — you think you're testing the module, but you're actually testing the cell override.

**Q: Do I need to close Jupyter to use git?**
A: No. Open a second terminal window (Cmd+N) or tab (Cmd+T). The Jupyter server keeps running in the first terminal. This is normal — most developers have multiple terminals open.

**Q: What does `git status` telling me "working tree clean" actually mean?**
A: It means every file on disk is identical to the last commit. If you expected changes to show up and they don't, the file on disk was never actually modified (see Pitfall 5).

**Q: What does "Your branch is ahead of 'origin/main' by N commits" mean?**
A: You have committed changes locally that haven't been pushed to GitHub yet. Run `git push origin main` to sync.

**Q: What does "Your branch is up to date with 'origin/main'" mean?**
A: Your last push is still the latest — local commits and GitHub match.

**Q: Should I use `git add .` or `git add <specific files>`?**
A: Use specific files (`git add bjerknes_physics.py Bjerknes-Diagnostic-Lab.ipynb`). Using `git add .` stages everything, including junk like `.ipynb_checkpoints/`. If you have a `.gitignore` that excludes such folders, `git add .` is safe.

**Q: What's `.ipynb_checkpoints/` and should I commit it?**
A: No. It's Jupyter's autosave folder. Add it to `.gitignore`:
```bash
echo ".ipynb_checkpoints/" > .gitignore
git add .gitignore
git commit -m "Add gitignore"
git push origin main
```

**Q: I made a mistake in a commit. Can I undo it?**
A: If you haven't pushed yet: `git reset HEAD~1` undoes the last commit but keeps your files. If you already pushed: it's safer to just fix the file and make a new commit rather than rewriting public history.

**Q: How do I check what's actually in a file on disk (not what Jupyter has in memory)?**
A: In the terminal: `cat bjerknes_physics.py` prints the file contents, or `wc -l bjerknes_physics.py` shows the line count. If it says 25 lines when you expect 111, the file hasn't been updated.

**Q: What does "the remote contains work that you do not have locally" mean?**
A: GitHub has at least one commit you don't have — most often because you edited a file on github.com and forgot. Run `git fetch origin` then compare `git log --oneline origin/main -5` against `git log --oneline main -5` to see what diverged, then reconcile with `git pull --rebase origin main` (see Pitfall 10–11).

**Q: I deleted a file and pushed. Is it really gone from GitHub?**
A: It's gone from the *current view* but still **in the history** — anyone can recover it from an older commit. Removing a file from history entirely requires rewriting history (`git filter-repo`) and a force-push, which is heavier and disturbs anyone who cloned the repo. For low-stakes files, removing from the current view is usually enough; for secrets or copyrighted material you never want recoverable, you need the full history scrub.

**Q: What's the difference between `git rm`, `git rm --cached`, and `.gitignore`?**
A: `git rm` deletes from git and disk. `git rm --cached` untracks from git but keeps the file on your disk (use this to stop publishing something you want to keep locally). `.gitignore` only prevents *future* tracking of files not already tracked — it does nothing to a file that's already committed (see Pitfall 13).

**Q: A rebase stopped and said CONFLICT. Did I break something?**
A: No. Git just can't auto-merge two edits to the same lines and is asking you to choose. Resolve the named file (keep yours with `git checkout --theirs FILE` during a rebase — note the flag is reversed in rebase), then `git add FILE` and `git rebase --continue`. If you'd rather start over, `git rebase --abort` returns you to before the pull (see Pitfall 12).

**Q: When should I make a backup branch?**
A: Before any operation that rewrites history — rebase, reset, or anything with `--force`. `git branch backup-before-X` is a free bookmark; if the operation goes wrong, you can return to it. Costs nothing, saves you from disasters.

**Q: I pushed 5 small edits. Does re-syncing the Claude Project cost a lot of tokens?**
A: The *edits* don't; the *file size* does. Sync re-loads the whole changed file, not your diff. If the file is a lean `.py` or an output-stripped notebook, it's cheap. If it's a notebook full of embedded plot images, it's expensive regardless of how small your edit was.

**Q: Is it cheaper to paste the changed section to Claude than to sync the repo?**
A: For a focused review, yes — much cheaper, because you skip the whole notebook JSON. Paste `git diff` output rather than two full copies. Use the sync when you actually need whole-project context (e.g. cross-notebook effects).

**Q: Why does my notebook take up so much of Claude's context when the code is short?**
A: A `.ipynb` stores cell outputs inline, including every plot as a base64 PNG blob. The images, not the code, dominate the token weight. Strip outputs (Pitfall 16) and the problem largely disappears.

**Q: Does Claude re-read the whole repo on every message?**
A: No. Within a conversation, project knowledge is cached — only new/uncached content counts. A full re-load happens when you click "Sync now," and only for the files that changed.

---

## Cheat Sheet

```
# Launch Jupyter from the repo (always do this)
cd /Users/dantsai/Documents/GitHub/Bjerknes-Diagnostic-Lab
jupyter notebook

# In a second terminal — the daily loop
cd /Users/dantsai/Documents/GitHub/Bjerknes-Diagnostic-Lab
git status                          # what changed?
git diff bjerknes_physics.py        # line-by-line changes
git add bjerknes_physics.py Bjerknes-Diagnostic-Lab.ipynb
git commit -m "What I changed and why"
git push origin main

# Emergency checks
wc -l bjerknes_physics.py           # how many lines? (25 = old, 111 = new)
cat bjerknes_physics.py             # print the actual file contents
git log --oneline -5                # last 5 commits
# When push is rejected (local and GitHub diverged)
git fetch origin                          # see remote state without merging
git log --oneline origin/main -5          # what's on GitHub
git log --oneline main -5                 # what's local
git branch backup-before-rebase           # SAFETY bookmark before reconciling
git pull --rebase origin main             # replay your commits on top of remote
#   if it stops on a conflict:
git checkout --theirs <file>              #   keep YOUR version (--theirs = yours, in rebase)
git add <file>; git rebase --continue
#   if it goes wrong:  git rebase --abort

# Stop publishing a file but keep it on your Mac
git rm --cached "file.pdf"                # untrack, keep on disk
echo "*.pdf" >> .gitignore                # prevent re-tracking

# Renaming a tracked notebook (close it in Jupyter first!)
git mv old.ipynb 01_new.ipynb
git diff --no-index old.ipynb 01_new.ipynb   # empty = safe; if old reappears, rm it

# Strip notebook outputs before committing (token tax + clean diffs)
jupyter nbconvert --clear-output --inplace 01_Bjerknes_Zonal_Diagnostic.ipynb
nbstripout --install                         # automate on every commit (run once in repo)

# Cheapest way to show Claude a change — paste this, NOT two full files
git diff bjerknes_physics.py                 # unstaged edits
git diff HEAD~1 bjerknes_physics.py          # vs. previous commit

# Claude Project sync — the mental model
#   - "Sync now" re-loads WHOLE changed files, not your diff  → keep files lean
#   - within one chat, synced knowledge is cached             → re-referencing is cheap
#   - hit "Sync now" at the START of a session where currency matters
```
