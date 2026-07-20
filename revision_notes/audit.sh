#!/usr/bin/env bash
# Reconcile-pass audit. Run from repo root: bash revision_notes/audit.sh
# Then paste the whole output into the chat to sync state with Claude.
set -uo pipefail
echo "========================================================"
echo "SELF-AUDIT  $(date '+%Y-%m-%d %H:%M')  branch: $(git branch --show-current)"
echo "========================================================"

echo; echo "--- A. TREE HONESTY ---"
git status -sb
echo "recent commits:"
git --no-pager log --oneline -8
echo "uncommitted diffstat:"
git --no-pager diff --stat

echo; echo "--- B. RECORD vs ARTIFACT ---"
echo "notebook exec counts. NB3 should be [1..N] (run, outputs baked in)."
echo "NB1/NB2 are intentionally output-stripped by nbstripout -> null is EXPECTED there."
echo "NB4 is a stub -> [None] expected. Only investigate a null in a notebook you"
echo "believe you just ran (e.g. NB3 showing null = it wasn't actually executed)."
python3 -c "import json,glob; [print(' ',f,'->',[c.get('execution_count') for c in json.load(open(f))['cells'] if c['cell_type']=='code']) for f in glob.glob('*.ipynb')]" 2>/dev/null || echo "  (python check skipped)"

echo; echo "--- C. ORPHANS / COLUMN-0 ESCAPES in tracker ---"
grep -nE "^(RESOLUTIONS|[0-9]+ Jul UPDATE)" revision_notes/task_B3_tracker.md || echo "  none (good)"
echo "numbered items 9/10 (should show one '9.' and one '10.', not two of either):"
grep -nE "^9\. |^10\. " revision_notes/task_B3_tracker.md

echo; echo "--- D. UNWANTED / SECRET FILES TRACKED ---"
git ls-files | grep -iE "data_SYNTHETIC|\.html$|_files/|\.nc$|token|secret|\.env" && echo "  ^^ REVIEW THESE" || echo "  none tracked (good)"

echo; echo "--- E. UNTRACKED (04_ is the only expected one) ---"
git ls-files --others --exclude-standard

echo; echo "--- F. TODAY (TODO.md head) ---"
sed -n '1,60p' TODO.md 2>/dev/null || echo "  TODO.md missing"

echo; echo "========================================================"
echo "AUDIT DONE — paste everything above into the chat to sync."
echo "========================================================"