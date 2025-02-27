def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 58:
        return nums[-2]
    else:
        return None