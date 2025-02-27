def sum_odd_ints_inclusive(ints_list):
    return sum((num for num in ints_list[80:201] if num % 2 != 0))