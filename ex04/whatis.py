import sys


def whatis(n):
    """This function prints whether the given integer is even or odd."""

    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    """This function is the main function."""

    sys.tracebacklimit = 0
    if len(sys.argv) == 1:
        sys.exit(1)
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if not sys.argv[1].isdigit():
        raise AssertionError("argument is not an integer")
    whatis(int(sys.argv[1]))


main()

# Output
"""
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
"""
