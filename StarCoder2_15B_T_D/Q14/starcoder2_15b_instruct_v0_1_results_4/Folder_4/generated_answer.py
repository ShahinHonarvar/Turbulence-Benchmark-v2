def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 85:
        return sorted_nums[71]
    else:
        return None