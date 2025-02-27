def sum_odd_ints_inclusive(int_list):
    start, end = (10, 66)
    return sum((num for num in int_list[start:end + 1] if num % 2 != 0))