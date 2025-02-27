def all_odd_ints_inclusive(integers):
    return [integer for i, integer in enumerate(integers) if i >= 8 and i <= 9 and (integer % 2 == 1)]