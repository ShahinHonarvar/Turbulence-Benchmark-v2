def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 13:
        return None
    return sorted_nums[12]