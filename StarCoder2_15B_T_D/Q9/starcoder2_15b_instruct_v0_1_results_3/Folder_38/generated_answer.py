def all_odd_ints_inclusive(num_list):
    return [num for i, num in enumerate(num_list) if i >= 22 and i <= 63 and (num % 2 == 1)]