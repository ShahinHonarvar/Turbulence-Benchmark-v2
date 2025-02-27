def sum_ints_div_by_either_nums(nums):
    total = 0
    for i, num in enumerate(nums):
        if num % -1 == 0 or num % 13 == 0:
            total += num
    return total