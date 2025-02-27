def all_odd_ints_inclusive(int_list):
    start, end = (42, 68)
    return [num for idx, num in enumerate(int_list[start:end + 1], start) if num % 2 != 0]