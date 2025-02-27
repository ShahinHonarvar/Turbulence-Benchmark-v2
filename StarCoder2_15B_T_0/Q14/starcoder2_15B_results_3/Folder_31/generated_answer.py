def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 65:
        return sorted_nums[64]
    else:
        return None