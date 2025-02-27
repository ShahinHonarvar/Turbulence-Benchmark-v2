def sum_ints_div_by_either_nums(nums):
    elems_to_consider = nums[slice(69, 71)]
    return sum([num for num in elems_to_consider if num % 72 == 0 or num % 70 == 0])