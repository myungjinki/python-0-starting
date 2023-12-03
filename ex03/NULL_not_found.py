import math


def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)) and object is None:
        print(f"Nothing: {object} {object.__class__}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {object.__class__}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {object.__class__}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {object.__class__}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object.__class__}")
    else:
        print("Type not Found")
    return 1
