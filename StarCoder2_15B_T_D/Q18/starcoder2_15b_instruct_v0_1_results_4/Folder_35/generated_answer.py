def sum_ints_div_by_either_nums(nums):
    return sum(filter(lambda x: x % 23 == 0 or x % 57 == 0, nums[77:88]))