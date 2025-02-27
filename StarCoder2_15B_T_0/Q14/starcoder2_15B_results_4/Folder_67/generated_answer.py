def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 54:
        return sorted_nums[51]
    else:
        return None