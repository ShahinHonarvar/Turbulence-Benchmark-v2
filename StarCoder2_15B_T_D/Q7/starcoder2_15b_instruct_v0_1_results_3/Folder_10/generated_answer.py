def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 25 to index 59, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_nums = []
    for i in range(25, 60):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums