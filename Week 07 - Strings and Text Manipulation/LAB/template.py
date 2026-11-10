from pathlib import Path
"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan Shine
Lane  :  AI 
Date  :  11/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Clean one raw line into a dict with lowercase keys and float values."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)

    fields = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return fields


def status_of(record):
    """Return OVER LIMIT, WARNING or OK based on the used/total percentage."""
    percent = record["used"] / record["total"] * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

with open(Path(__file__).parent / "raw_lines.txt") as f:
    raw_records = [line for line in f if line.strip() != ""]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, status)
    if status != "OK":
        flagged += 1

print(f"{len(raw_records)} records, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring

