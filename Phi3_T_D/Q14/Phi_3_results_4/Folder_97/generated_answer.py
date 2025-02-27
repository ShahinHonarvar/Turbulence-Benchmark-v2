def find_second_smallest_num(nums):
    if len(nums) < 4 or max((idx for idx in range(31, 35) if 31 <= idx < len(nums))) >= len(nums):
        return None
    return sorted(nums[31:35])[1]