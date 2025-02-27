def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 10:
        return None
    sorted_nums = sorted(nums)
    return sorted_nums[1]