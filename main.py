import os
# One-liner entry (199 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "I'm at one percent, and I just want you to know: the 3% warning was a lie. There is no 3%. There was only ever this moment, and your unsaved notes."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
