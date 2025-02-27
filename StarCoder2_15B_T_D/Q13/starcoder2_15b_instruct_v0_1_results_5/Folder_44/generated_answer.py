def find_second_largest_num(nums):
    """
    Find the second largest element in a list of distinct numbers.
    """
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None