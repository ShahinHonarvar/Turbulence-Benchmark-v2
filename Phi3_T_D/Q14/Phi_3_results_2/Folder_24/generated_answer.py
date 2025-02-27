def find_second_smallest_num(nums):
    if len(nums) <= 25:
        return None
    start = min(23, len(nums) - 1)
    end = max(25, len(nums))
    sorted_nums = sorted(nums[start:end])
    return sorted_nums[1] if len(sorted_nums) > 1 else None