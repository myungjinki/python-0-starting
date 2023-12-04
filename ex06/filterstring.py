import sys

from ft_filter import ft_filter


sys.tracebacklimit = 0


def filterstring(string, length):
    """a list of words from S that have a length greater than N."""

    lst = [word for word in string.split()]
    return ft_filter(lambda x: len(x) > length, lst)


def main():
    """Main function."""

    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    s = sys.argv[1]
    n = sys.argv[2]
    try:
        length = int(n)
    except ValueError:
        raise AssertionError("the arguments are bad")
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
