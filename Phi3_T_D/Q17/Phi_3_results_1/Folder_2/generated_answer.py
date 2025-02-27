def all_ints_div_by_both_two_nums(lst):
    """Return list of integers divisible by both 54 and 82 from index 73 to 86."""
    desired_indices = range(73, 87)
    divisible_ints = [num for index, num in enumerate(lst) if index in desired_indices and num % 54 == 0 and (num % 82 == 0)]
    return divisible_ints