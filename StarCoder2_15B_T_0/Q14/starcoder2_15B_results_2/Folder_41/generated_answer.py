def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 4:
        return sorted_nums[4]
    else:
        return None