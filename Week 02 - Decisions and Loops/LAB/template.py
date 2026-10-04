"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan Shine
Lane  :  AI
Date  :  10/2/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
over_limit_count = 0
while True:
    label = input("Dataset name (or quit): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = limit - value                        # rows still missing
percent = value / limit * 100

# 3. Decide a status and store it in a variable called status.

if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"



# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print("=" * 34)
print(f"  RECORD CHECK  - ", label)
print("=" * 34)

print(f"  Loaded    : {value:>10.2f}")
print(f"  Expected  : {limit:>10.2f}")
print(f"  Missing   : {difference:>10.2f}")
print(f"  Percent   : {percent:>10.2f} %")
print(f"  Status    : {status:>10}")

print("=" * 34)

print("Records OVER LIMIT:", over_limit_count)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
