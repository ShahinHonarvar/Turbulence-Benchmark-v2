def find_second_smallest_num(numbers):
    """
    Find the second smallest element in the list `numbers` from index 28 to 38, both inclusive.
    If there is no such an element, return None.
    """
    sorted_numbers = sorted(numbers[28:39])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]