import sys


def whatis(n):
    if not isinstance(n, int):
        raise AssertionError("argument is not an integer")
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:
        whatis(int(sys.argv[1]))
    except ValueError as e:
        print("AssertionError: argument is not an integer")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
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