def sum_even_ints_inclusive(int_list):
    sum_even = sum([num for num in int_list[:2] if num % 2 == 0])
    return sum_even