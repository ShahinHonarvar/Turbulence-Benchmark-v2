def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 64:
        return sorted_nums[63]
    else:
        return None