def all_even_ints_inclusive(nums):
    """Return the list of all even integers from index 4 to index 8, both inclusive. If no even integers exist in the specified range, return an empty list."""
    return [num for num in nums[4:9] if num % 2 == 0]