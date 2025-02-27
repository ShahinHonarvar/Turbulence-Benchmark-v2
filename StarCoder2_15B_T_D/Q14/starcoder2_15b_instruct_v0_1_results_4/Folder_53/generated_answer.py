def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 2 or len(sorted_nums) < 101:
        return None
    return sorted_nums[1]