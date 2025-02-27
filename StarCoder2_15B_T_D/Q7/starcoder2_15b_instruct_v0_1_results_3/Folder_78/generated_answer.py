def all_even_ints_inclusive(ints_list):
    return [num for idx, num in enumerate(ints_list) if idx >= 43 and idx <= 51 and (num % 2 == 0)]