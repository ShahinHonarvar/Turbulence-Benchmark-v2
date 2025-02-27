def find_second_largest_num(nums):
    if len(nums) > 5:
        nums = nums[:6]
    sorted_nums = sorted(set(nums), reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None