"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan
Lane  :  AI      (delete two)
Date  :  23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns OVER LIMIT, WARNING, OK"""
        percent = (self.value / self.limit) * 100
        result = "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
        return result
    


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
def load_records(path):
    records = []   # replace with your code
    with open(path) as f:
        for i in f:
            label, value, limit = i.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("Week 05 - Classes and Objects/LAB/my_records.txt")        


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
over_limit_count = 0
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    result = record.status()
    print(f"    Dataset         : {record.label}")
    print(f"    Rows loaded     : {record.value}")
    print(f"    Rows expected   : {record.limit}")
    print(f"    Status          : {result}")
    if result == "OVER LIMIT":
        over_limit_count += 1
    print("=" * 34)
print()
print(over_limit_count, "of", len(records), "records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
