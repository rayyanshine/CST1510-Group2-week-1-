"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan Shine
Lane  :  AI 
Date  :  10/17/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """give difference, percent and status for 1 record"""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints full bordered report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Loaded       : {value:>10.2f}")
    print(f"  Expected     : {limit:>10.2f}")
    print(f"  Missing      : {difference:>10.2f}")
    print(f"  Percent      : {percent:>10.2f}")
    print(f"  Status       : {status:>10}")
    print("=" * 34)



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
def load_records(path):
    """reads label, value and limit lines from the file and returns a list of dictionary"""
    records = []
    with open(path) as f:
        for i in f:
            label, value, limit = i.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records
    
try:
    records = load_records("my_data.txt")
except FileNotFoundError:
    print("could not find my_data.txt file")
    records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit = 0
with open("results.txt", "w") as f:
    for i in records:
        label = i["label"]
        value = i["value"]
        limit = i["limit"]
        difference, percent, status = check_record(value, limit)
        print_report(label, value, limit, difference, percent, status)
        f.write(f"{label},{status}\n")
        if status == "OVER LIMIT":
            over_limit += 1
print(f"{over_limit} of {len(records)} were over limit")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
