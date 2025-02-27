def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 30 to index 200, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """

    def is_even(num):
        return num % 2 == 0
    result = [num for num in nums[30:201] if is_even(num)]
    return result