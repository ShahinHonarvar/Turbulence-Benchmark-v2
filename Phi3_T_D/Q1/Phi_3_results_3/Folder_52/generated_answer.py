def all_ints_inclusive(integers):
    if len(integers) > 78:
        return integers[62:79]
    return integers[max(0, len(integers) - 79):len(integers) - 61] if len(integers) > 59 else []