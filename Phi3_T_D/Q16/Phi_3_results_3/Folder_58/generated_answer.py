def sum_even_ints_inclusive(int_list):
    return sum((num for idx, num in enumerate(int_list[209:557], start=209) if num % 2 == 0))