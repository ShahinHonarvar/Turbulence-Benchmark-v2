def all_odd_ints_inclusive(integers):
    start = 42
    end = 68
    return [x for x in integers[start:end + 1] if x % 2 != 0]