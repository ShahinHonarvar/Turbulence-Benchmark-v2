def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[:1] if abs(num) % 1 == 0))