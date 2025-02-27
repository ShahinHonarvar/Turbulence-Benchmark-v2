def sum_even_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list) if i >= 25 and i <= 59 and (num % 2 == 0)))