def all_odd_ints_inclusive(nums):
    """
    Return the list of all odd integers from index 667 to index 774, both inclusive.
    If no odd integers exist in the specified range, return an empty list.
    """
    return [num for i, num in enumerate(nums) if i >= 667 and i <= 774 and (num % 2 == 1)]