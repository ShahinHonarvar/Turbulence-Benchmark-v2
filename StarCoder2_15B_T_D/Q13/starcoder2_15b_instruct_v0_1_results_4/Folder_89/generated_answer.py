def find_second_largest_num(nums):
    nums_sliced = nums[56:83]
    nums_sliced.sort(reverse=True)
    if len(nums_sliced) >= 2:
        return nums_sliced[1]
    else:
        return None