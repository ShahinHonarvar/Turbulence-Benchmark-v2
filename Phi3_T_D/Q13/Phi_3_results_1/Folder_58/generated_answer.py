def find_second_largest_num(nums):
    if not 209 <= len(nums) < 557:
        return None
    unique_nums = sorted(set(nums[209:557]), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None