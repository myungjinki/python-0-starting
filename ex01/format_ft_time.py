import time
import datetime

# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/time.html#time.time
# time.time() returns the number of seconds since January 1, 1970, 00:00:00
seconds_since_epoch = time.time()

# https://docs.python.org/3/library/string.html#format-string-syntax
# grouping_option ::=  "_" | ","
# type - f: floating point number
# type - e: floating point number in exponential notation
result = f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or \
{seconds_since_epoch:.2e} in scientific notation"
print(result)

# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
day = datetime.datetime.now()
print(f"{day:%b %d %Y}")
