from the given list `nums`. If no positive integers exist in the specified range,

def all_pos_ints_inclusive(nums):
    """
    Returns a list of all positive integers from index 686 to index 987, both inclusive,
    an empty list is returned.
    """
    return [num for num in nums[686:988] if num > 0]