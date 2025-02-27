def sum_ints_div_by_either_nums(nums):
    total = 0
    for i, num in enumerate(nums):
        if num % -20 == 0 or num % -26 == 0:
            if 25 <= i <= 80:
                total += num
    return total