def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 151:
        return sorted_nums[150]
    else:
        return None