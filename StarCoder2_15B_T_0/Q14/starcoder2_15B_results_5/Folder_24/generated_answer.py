def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 24:
        return sorted_nums[23]
    else:
        return None