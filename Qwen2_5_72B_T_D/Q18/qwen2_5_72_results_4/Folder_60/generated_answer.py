def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[10:80]:
        if num % -74 == 0 or num % -58 == 0:
            total += num
    return total