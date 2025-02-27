def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 209 and len(sorted_nums) >= 556:
        return sorted_nums[209:556][1]
    else:
        return None