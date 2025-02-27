def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) < 67:
        return None
    return sorted_nums[10:67][1]