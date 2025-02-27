def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 94:
        return []
    return [n for n in nums[14:94] if n % 71 == 0 and n % 81 == 0]