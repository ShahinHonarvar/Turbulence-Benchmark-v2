def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_max = max(nums[0], nums[1])
    second_max = min(nums[0], nums[1])
    return second_max if first_max != second_max else None