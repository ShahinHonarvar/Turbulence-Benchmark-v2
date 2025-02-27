def all_ints_div_by_both_two_nums(lst):
    """Return integers divisible by both 2 and 3 from index 7 to index 9."""
    divisible_elements = [num for num in lst[7:10] if num % 2 == 0 and num % 3 == 0]
    return divisible_elements