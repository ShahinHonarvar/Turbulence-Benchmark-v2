def all_even_ints_inclusive(int_list):
    start, end = (667, 774)
    return [num for num in int_list[start:end + 1] if num % 2 == 0]