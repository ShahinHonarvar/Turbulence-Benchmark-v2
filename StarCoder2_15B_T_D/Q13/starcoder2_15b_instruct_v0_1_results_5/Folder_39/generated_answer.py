def find_second_largest_num(nums):
    nums_sliced = nums[20:31]
    nums_sliced.sort(reverse=True)
    if len(nums_sliced) < 2:
        return None
    return nums_sliced[1]