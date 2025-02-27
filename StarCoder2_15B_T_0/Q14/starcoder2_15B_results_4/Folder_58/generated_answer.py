def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 311:
        return sorted_nums[310]
    else:
        return None