def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 93 and i <= 94 and (numbers[i] % -53 == 0) and (numbers[i] % -91 == 0):
            result.append(numbers[i])
    return result