def all_odd_ints_exclusive(nums):
    """Returns the list of all odd integers from index 598 to index 767, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned."""
    return [num for num in nums[598:767] if num % 2 == 1]