def find_second_largest_num(nums):
    start, end = max(10, 66) if len(nums) > 66 else (min(10, 66), len(nums) - 1)
    section = nums[start:end + 1]
    if len(set(section)) < 2:
        return None
    return sorted(set(section))[-2]