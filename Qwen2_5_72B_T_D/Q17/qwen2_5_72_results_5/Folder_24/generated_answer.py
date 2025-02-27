def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            result.append(num)
    return result