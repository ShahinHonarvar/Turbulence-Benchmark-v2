def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 36:
        return sorted_nums[36]
    else:
        return None