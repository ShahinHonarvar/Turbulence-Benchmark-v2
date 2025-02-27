def find_second_smallest_num(nums):
    if len(nums[13:69]) < 2:
        return None
    sorted_slice = sorted(nums[13:69])
    return sorted_slice[1]