def find_second_largest_num(nums):
    """
    Finds the second largest element from index 22 to index 50, both inclusive.
    If there is no such element, returns 'None'.
    """
    nums_subset = nums[22:51]
    max_num = max(nums_subset)
    second_largest_num = max([num for num in nums_subset if num < max_num])
    return second_largest_num