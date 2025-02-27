def find_second_largest_num(nums):
    nums_slice = nums[56:67]
    sorted_slice = sorted(nums_slice, reverse=True)
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None