def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 83:
        return sorted_nums[56]
    else:
        return None