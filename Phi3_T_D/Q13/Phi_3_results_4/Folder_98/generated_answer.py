def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sorted_nums = sorted(nums[:7])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]