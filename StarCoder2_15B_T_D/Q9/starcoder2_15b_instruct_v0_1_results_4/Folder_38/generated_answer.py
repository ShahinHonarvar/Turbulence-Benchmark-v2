from the given list of integers. If no odd integers exist in the specified range,

def all_odd_ints_inclusive(nums):
    """
    Returns the list of all odd integers from index 22 to index 63, both inclusive,
    an empty list is returned.
    """
    return [num for i, num in enumerate(nums) if i >= 22 and i <= 63 and (num % 2 == 1)]