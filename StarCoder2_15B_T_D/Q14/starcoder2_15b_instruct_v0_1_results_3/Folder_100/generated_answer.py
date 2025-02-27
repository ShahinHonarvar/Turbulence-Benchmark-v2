def find_second_smallest_num(numbers):
    """
    Find the second smallest element from index 43 to index 51, both inclusive.
    If there is no such an element, return 'None'.
    """
    sublist = sorted(numbers[43:52])
    if len(sublist) < 2:
        return None
    return sublist[1]