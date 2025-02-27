def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 99:
        return None
    return nums[-2]