def all_odd_ints_inclusive(ints):
    if len(ints) <= 60:
        return []
    return [num for num in ints[60:71] if num % 2 != 0]