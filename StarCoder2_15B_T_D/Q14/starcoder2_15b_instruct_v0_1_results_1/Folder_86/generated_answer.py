def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 33:
        return sorted_nums[33]
    else:
        return None