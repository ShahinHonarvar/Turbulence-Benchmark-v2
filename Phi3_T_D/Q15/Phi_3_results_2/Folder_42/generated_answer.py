def sum_odd_ints_inclusive(int_list):
    total = sum((num for num in int_list[29:80] if num % 2 == 1))
    return total