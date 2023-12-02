import sys

from ft_filter import ft_filter


def filterstring(string, length):
    """a list of words from S that have a length greater than N."""

    return ft_filter(lambda x: len(x) > length, [word for word in string.split()])


def main():
    """Main function."""

    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    s = sys.argv[1]
    n = sys.argv[2]
    try:
        length = int(n)
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    print(filterstring(s, length))


if __name__ == "__main__":
    main()

# Output when run:
"""
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>

$> python filterstring.py 'Hello the World' 99
[]
$>

$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>

$> python filterstring.py
AssertionError: the arguments are bad
$>
"""
