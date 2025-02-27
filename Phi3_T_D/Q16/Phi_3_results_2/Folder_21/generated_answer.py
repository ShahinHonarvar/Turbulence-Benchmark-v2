def sum_even_ints_inclusive(int_list):
    start_idx, end_idx = (639, 975)
    return sum((num for num in int_list[start_idx:end_idx + 1] if num % 2 == 0))