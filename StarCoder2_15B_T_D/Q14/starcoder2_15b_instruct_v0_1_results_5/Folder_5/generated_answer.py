def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) > 5:
        return sorted_nums[3]
    else:
        return None