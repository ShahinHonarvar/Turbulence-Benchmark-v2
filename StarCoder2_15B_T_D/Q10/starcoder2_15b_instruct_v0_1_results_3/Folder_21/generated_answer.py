def all_odd_ints_exclusive(integers):
    return [integer for i, integer in enumerate(integers) if i >= 743 and i < 867 and (integer % 2 == 1)]