import sys


sys.tracebacklimit = 0


def building(text):
    """This function prints the number of upper letters, lower letters,"""

    if not isinstance(text, str):
        raise AssertionError("argument is not a string")
    if len(text) == 0:
        print("The text contains 0 characters:")
        print("0 upper letters")
        print("0 lower letters")
        print("0 punctuation marks")
        print("0 spaces")
        print("0 digits")
        return
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            punct += 1
    print("The text contains {} characters:".format(len(text)))
    print("{} upper letters".format(upper))
    print("{} lower letters".format(lower))
    print("{} punctuation marks".format(punct))
    print("{} spaces".format(space))
    print("{} digits".format(digit))


def main():
    """
    This function is the main function.

    https://docs.python.org/3/library/io.html?highlight=readlines#i-o-base-classes
    """

    if len(sys.argv) == 1:
        try:
            print("What is the text to count?")
            input_text = sys.stdin.readline()
        except EOFError:
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            raise KeyboardInterrupt
    elif len(sys.argv) == 2:
        input_text = sys.argv[1]
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    building(input_text)


if __name__ == "__main__":
    main()


# Output
"""
$>python building.py "Python 3.0, released in 2008, was a major revision \
that is not completely backward-compatible with earlier versions. Python \
2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
"""

"""
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
"""
