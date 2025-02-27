def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 39:
        return None
    return sorted_nums[-2]