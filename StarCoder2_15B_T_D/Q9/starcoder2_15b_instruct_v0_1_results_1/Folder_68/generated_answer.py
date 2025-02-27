def all_odd_ints_inclusive(nums):
    """Returns the list of all odd integers from index 0 to index 8, both inclusive."""
    return [num for i, num in enumerate(nums) if i >= 0 and i <= 8 and (num % 2 == 1)]