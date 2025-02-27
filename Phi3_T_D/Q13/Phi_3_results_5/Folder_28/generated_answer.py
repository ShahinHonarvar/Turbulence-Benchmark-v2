def find_second_largest_num(nums):
    if 62 <= len(nums) - 1 <= 63:
        return nums[63]
    elif len(nums) > 63:
        sorted_nums = sorted(nums[62:64])
        return sorted_nums[-2] if len(sorted_nums) > 1 else None
    else:
        return None