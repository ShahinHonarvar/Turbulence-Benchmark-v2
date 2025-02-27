def find_second_smallest_num(nums):
    if len(nums) <= 57 or len(nums) < 6:
        return None
    sliced_nums = sorted(nums[56:58])
    return sliced_nums[1] if len(sliced_nums) == 2 else None