def find_second_largest_num(nums):
    nums_sliced = nums[90:91]
    nums_sliced.sort(reverse=True)
    if len(nums_sliced) < 2:
        return None
    return nums_sliced[1]