def find_second_largest_num(nums):
    if len(nums) <= 8:
        return None
    limited_nums = nums[:9]
    limited_nums.sort()
    return limited_nums[-2]