def find_second_largest_num(nums):
    if len(nums[3:6]) < 2:
        return None
    sorted_slice = sorted(nums[3:6], reverse=True)
    return sorted_slice[1]