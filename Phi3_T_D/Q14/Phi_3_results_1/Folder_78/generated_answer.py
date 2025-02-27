def find_second_smallest_num(nums):
    valid_indices_nums = nums[17:79]
    if len(valid_indices_nums) < 2:
        return None
    sorted_nums = sorted(valid_indices_nums)
    return sorted_nums[1]