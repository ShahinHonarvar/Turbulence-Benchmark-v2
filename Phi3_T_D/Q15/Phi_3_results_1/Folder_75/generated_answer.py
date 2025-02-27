def sum_odd_ints_inclusive(int_list):
    if len(int_list) <= 57:
        return 0
    return sum((num for num in int_list[56:58] if num % 2 != 0))