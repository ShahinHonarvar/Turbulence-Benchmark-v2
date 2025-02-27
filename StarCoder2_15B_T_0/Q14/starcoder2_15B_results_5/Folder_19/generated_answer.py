def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 6:
        return sorted_nums[5]
    else:
        return None