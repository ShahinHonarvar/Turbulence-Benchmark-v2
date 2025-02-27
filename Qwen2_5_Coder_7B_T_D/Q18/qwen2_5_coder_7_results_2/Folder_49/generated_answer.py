def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[80:201]) if x % 10 == 0 or x % 1000 == 0))