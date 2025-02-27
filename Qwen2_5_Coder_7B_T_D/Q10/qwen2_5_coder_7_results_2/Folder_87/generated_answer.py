def all_odd_ints_exclusive(num_list):
    return [num for i, num in enumerate(num_list) if i > 32 and i < 99 and (num % 2 != 0)]