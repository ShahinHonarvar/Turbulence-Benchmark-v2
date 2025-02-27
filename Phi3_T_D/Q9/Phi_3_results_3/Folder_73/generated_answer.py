def all_odd_ints_inclusive(int_list):
    start, end = (19, 92)
    odd_ints = [num for num in int_list[start:end + 1] if num % 2 != 0]
    return odd_ints