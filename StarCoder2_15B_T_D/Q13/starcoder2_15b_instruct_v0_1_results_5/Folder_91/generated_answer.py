def find_second_largest_num(nums):
    nums_copy = nums[:]
    nums_copy.sort(reverse=True)
    if len(nums_copy) < 2:
        return None
    return nums_copy[1]