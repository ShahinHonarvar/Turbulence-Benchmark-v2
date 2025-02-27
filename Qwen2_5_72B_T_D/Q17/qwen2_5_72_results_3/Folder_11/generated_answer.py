def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(22, 25):
        if numbers[i] % -85 == 0 and numbers[i] % -30 == 0:
            result.append(numbers[i])
    return result