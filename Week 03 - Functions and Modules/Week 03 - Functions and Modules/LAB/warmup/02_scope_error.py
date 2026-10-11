# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status # you send it out

status = check(87, 100) # you catch it

print(status) # now it exists
