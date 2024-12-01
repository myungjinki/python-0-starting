import sys


def sos(morse_code, morese_dict):
    """Convert morse code to text."""

    ret = "".join([morese_dict[char] for char in morse_code])
    return ret[:-1] if ret[-1] == " " else ret


def ismorse(morse_code, morese_dict):
    """Check if the morse code is valid."""

    for char in morse_code:
        if char not in morese_dict.keys():
            return False
    return True


def main():
    """Main function."""

    sys.tracebacklimit = 0
    # https://en.wikipedia.org/wiki/Morse_code
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "a": ".- ",
        "b": "-... ",
        "c": "-.-. ",
        "d": "-.. ",
        "e": ". ",
        "f": "..-. ",
        "g": "--. ",
        "h": ".... ",
        "i": ".. ",
        "j": ".--- ",
        "k": "-.- ",
        "l": ".-.. ",
        "m": "-- ",
        "n": "-. ",
        "o": "--- ",
        "p": ".--. ",
        "q": "--.- ",
        "r": ".-. ",
        "s": "... ",
        "t": "- ",
        "u": "..- ",
        "v": "...- ",
        "w": ".-- ",
        "x": "-..- ",
        "y": "-.-- ",
        "z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    morse_code = sys.argv[1]
    if not ismorse(morse_code, NESTED_MORSE):
        raise AssertionError("the arguments are bad")
    print(sos(morse_code, NESTED_MORSE))


if __name__ == "__main__":
    main()

# Output

"""
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
"""
