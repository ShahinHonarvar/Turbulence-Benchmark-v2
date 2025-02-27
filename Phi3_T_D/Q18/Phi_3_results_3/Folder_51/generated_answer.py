def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[6:10] if x % -1 == 0 or x % -10 == 0))