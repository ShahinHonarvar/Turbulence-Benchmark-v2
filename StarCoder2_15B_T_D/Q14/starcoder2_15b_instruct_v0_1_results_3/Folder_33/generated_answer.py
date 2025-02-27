def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 263:
        return sorted_nums[262]
    else:
        return None