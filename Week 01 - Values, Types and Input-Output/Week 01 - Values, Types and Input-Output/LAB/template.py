"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan Shine
Lane  :  AI
Date  :  9/26/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

dataset_name = input("Dataset: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = rows_loaded - rows_expected
percentage = (rows_loaded / rows_expected) * 100
rows_remaining = rows_expected - rows_loaded

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f" RECORD CHECK - {dataset_name}")
print("=" * 34)

print(f"Rows loaded  : {rows_loaded:>10.2f}")
print(f"Rows expected: {rows_expected:>10.2f}")
print(f"Difference   : {difference:>+10.2f}")
print(f"Percentage   : {percentage:>10.2f}%")
print(f"Rows remaining : {rows_remaining:>6.0f}")  # how many more rows need to load

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
