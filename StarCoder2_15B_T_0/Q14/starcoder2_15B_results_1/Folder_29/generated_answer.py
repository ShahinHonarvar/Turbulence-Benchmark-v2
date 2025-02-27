def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 59:
        return sorted_nums[58]
    else:
        return None