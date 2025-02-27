def sum_ints_div_by_either_nums(nums):
    return sum(filter(lambda x: x % 76 == 0 or x % 60 == 0, nums[78:82]), 0)