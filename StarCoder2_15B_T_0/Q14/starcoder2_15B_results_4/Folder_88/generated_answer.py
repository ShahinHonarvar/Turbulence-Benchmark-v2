def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 8:
        return sorted_nums[7]
    else:
        return None