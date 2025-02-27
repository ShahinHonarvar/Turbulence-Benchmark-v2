def find_second_largest_num(nums):
    if not 667 <= len(nums) <= 774:
        return None
    sorted_nums = sorted(nums[667:775], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None