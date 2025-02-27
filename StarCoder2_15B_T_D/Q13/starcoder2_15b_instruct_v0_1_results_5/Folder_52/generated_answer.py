def find_second_largest_num(nums):
    nums_sliced = nums[28:39]
    nums_sliced.sort(reverse=True)
    return nums_sliced[1] if len(nums_sliced) > 1 else None