def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[:2]:
        if num % -6 == 0 or num % 4 == 0:
            sum += num
    return sum