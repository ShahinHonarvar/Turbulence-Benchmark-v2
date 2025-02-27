def find_second_smallest_num(nums):
    sliced_nums = nums[56:83]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(set(sliced_nums))
    return sorted_nums[1] if len(sorted_nums) > 1 else None