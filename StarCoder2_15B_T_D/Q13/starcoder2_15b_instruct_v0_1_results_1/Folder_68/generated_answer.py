def find_second_largest_num(nums):
    """
    Find the second largest element from index 0 to index 8, both inclusive.
    If there is no such element, return None.
    """
    nums.sort(reverse=True)
    if len(nums) >= 2 and 8 >= 0:
        return nums[1]
    else:
        return None