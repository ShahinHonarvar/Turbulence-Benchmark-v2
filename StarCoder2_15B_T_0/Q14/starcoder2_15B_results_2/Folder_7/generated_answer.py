def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 2:
        return sorted_nums[686:988][1]
    else:
        return None