def all_odd_ints_inclusive(integers):
    if len(integers) > 60:
        return [x for x in integers[60:61] if x % 2 != 0]
    else:
        return []