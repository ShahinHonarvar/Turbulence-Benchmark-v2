def find_second_largest_num(nums):
    if len(nums) < 4 or len(nums) > 4:
        return None
    sliced_nums = sorted(nums[33:37], reverse=True)
    return sliced_nums[1] if len(sliced_nums) > 1 else None