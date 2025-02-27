def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 609:
        return sorted_nums[608]
    else:
        return None