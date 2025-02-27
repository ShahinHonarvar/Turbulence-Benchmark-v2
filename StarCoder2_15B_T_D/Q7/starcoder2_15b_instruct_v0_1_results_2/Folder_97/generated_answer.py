def all_even_ints_inclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 40 and i <= 80 and (num % 2 == 0)]