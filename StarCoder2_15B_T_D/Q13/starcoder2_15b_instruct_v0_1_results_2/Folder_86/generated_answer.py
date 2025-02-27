def find_second_largest_num(nums):
    nums_slice = nums[31:35]
    nums_slice.sort(reverse=True)
    if len(nums_slice) < 2:
        return None
    else:
        return nums_slice[1]