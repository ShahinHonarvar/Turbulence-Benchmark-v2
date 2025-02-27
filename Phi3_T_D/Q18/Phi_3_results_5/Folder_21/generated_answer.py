def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 934:
        return 0
    divisibles = [i for i in nums[315:935] if i % -897 == 0 or i % -556 == 0]
    return sum(divisibles)