def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 6:
        return None
    else:
        return nums[-2]