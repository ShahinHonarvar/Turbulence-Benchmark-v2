def all_odd_ints_exclusive(integers):
    return [integer for i, integer in enumerate(integers) if i % 2 == 1 and 0 < i < 6]