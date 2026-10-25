qa_evidence=$(mktemp -d "${TMPDIR:-/tmp}/qa-procedure.XXXXXX") && printf '%s
' "$qa_evidence"

node --test tests/template-contract.test.mjs > "$qa_evidence/template-contract.txt" 2>&1
qa_exit=$?
printf 'exit_code=%s
' "$qa_exit" >> "$qa_evidence/template-contract.txt"
cat "$qa_evidence/template-contract.txt"
