def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 81:
        return None
    eligible_nums = sorted(nums[12:93])
    if len(eligible_nums) < 2:
        return None
    return eligible_nums[1]