def all_even_ints_inclusive(input_list):
    return [num for idx, num in enumerate(input_list) if idx >= 8 and idx <= 9 and (num % 2 == 0)]