def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(29, 54):
        if numbers[i] % -68 == 0 and numbers[i] % -85 == 0:
            result.append(numbers[i])
    return result