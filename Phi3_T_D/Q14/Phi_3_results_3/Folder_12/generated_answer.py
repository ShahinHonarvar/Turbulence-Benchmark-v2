def find_second_smallest_num(nums):
    sliced_nums = nums[31:73]
    if len(sliced_nums) < 2:
        return None
    unique_nums = sorted(set(sliced_nums))
    return unique_nums[1] if len(unique_nums) > 1 else None