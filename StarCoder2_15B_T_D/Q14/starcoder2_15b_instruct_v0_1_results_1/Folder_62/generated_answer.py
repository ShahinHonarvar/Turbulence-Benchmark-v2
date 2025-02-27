def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 67:
        return sorted_nums[10:67][1]
    else:
        return None