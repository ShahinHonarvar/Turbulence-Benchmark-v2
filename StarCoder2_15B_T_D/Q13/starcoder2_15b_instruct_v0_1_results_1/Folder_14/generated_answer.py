def find_second_largest_num(nums):
    nums_slice = nums[5:8]
    nums_slice.sort(reverse=True)
    if len(nums_slice) >= 2:
        return nums_slice[1]
    else:
        return None