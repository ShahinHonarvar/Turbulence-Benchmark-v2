def all_pos_ints_exclusive(numbers):
    """
    Takes a list of integers and returns the list of all positive integers from index 323 to index 972, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = [number for number in numbers[323:972] if number > 0]
    return result