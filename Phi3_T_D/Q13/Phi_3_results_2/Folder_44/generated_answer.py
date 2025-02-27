def find_second_largest_num(nums):
    sliced = nums[13:69]
    if len(sliced) < 2:
        return None
    sorted_slice = sorted(sliced, reverse=True)
    return sorted_slice[1]