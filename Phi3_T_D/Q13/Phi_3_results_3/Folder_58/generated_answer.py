def find_second_largest_num(nums):
    start = max(209, len(nums))
    end = min(556, len(nums)) + 1
    if start > end:
        return None
    sorted_nums = sorted(nums[start - 1:end], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None