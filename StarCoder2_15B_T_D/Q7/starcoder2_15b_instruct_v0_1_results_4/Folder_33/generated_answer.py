def all_even_ints_inclusive(nums):
    """Returns the list of all even integers from index 667 to index 774, both inclusive."""
    return [num for i, num in enumerate(nums) if i >= 667 and i <= 774 and (num % 2 == 0)]