def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 21:
        return sorted_nums[21]
    else:
        return None