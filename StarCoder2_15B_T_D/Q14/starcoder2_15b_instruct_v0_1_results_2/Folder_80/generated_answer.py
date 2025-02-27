def find_second_smallest_num(nums):
    """
    Find the second smallest element from index 30 to index 87, both inclusive,
    or `None` if there is no such an element.
    """
    nums.sort()
    if len(nums) > 87:
        return nums[31]
    else:
        return None