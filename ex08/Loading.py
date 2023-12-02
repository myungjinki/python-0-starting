import os
import sys

LEN = 40


def write(str):
    """sys.stdout.write(str)"""

    sys.stdout.write(str)


def print_percentage(i, len):
    """Print percentage of progress"""

    res = int(i / len * 100)
    write(f"{res}%")


def print_status_bar(i, len):
    """Print status bar of progress"""

    column = os.get_terminal_size().columns - LEN
    if column < 0:
        column = 1
    ret = "█" * int(column * i / len)
    write(f"|{ret:{column}s}| ")


def print_count(i, len):
    """Print count of progress"""

    write(f"{i}/{len}")


def ft_tqdm(lst: range) -> None:
    """
    Example

    100%|[===============================================================>]| 333/333
    100%|                                                                  | 333/333 [00:01<00:00, 191.61it/s]
    """
    length = len(lst)

    for i, element in enumerate(lst):
        i = i + 1
        sys.stdout.write("\r")
        print_percentage(i, length)
        print_status_bar(i, length)
        print_count(i, length)
        sys.stdout.flush()
        yield
