def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) > 10:
        return sorted_nums[-2]
    else:
        return None