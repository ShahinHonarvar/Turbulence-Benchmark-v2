def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) > 77:
        return sorted_nums[66]
    else:
        return None