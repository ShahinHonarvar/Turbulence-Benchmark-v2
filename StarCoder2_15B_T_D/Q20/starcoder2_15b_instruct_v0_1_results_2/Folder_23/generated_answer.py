def find_n_th_smallest_num(numbers):
    """
    Finds the 13th smallest number from index 14 to index 96 in a list of distinct numbers.
    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[13 + 14]