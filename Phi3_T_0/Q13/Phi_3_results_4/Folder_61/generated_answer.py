def find_second_largest_num(nums):
    if len(nums) < 2 or max(nums[:8]) == min(nums[:8]):
        return None
    sorted_nums = sorted(nums[:8], reverse=True)
    return sorted_nums[1]