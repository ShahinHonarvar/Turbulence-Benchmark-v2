def all_even_ints_exclusive(num_list):
    return [num for i, num in enumerate(num_list) if i >= 48 and i < 76 and (num % 2 == 0)]