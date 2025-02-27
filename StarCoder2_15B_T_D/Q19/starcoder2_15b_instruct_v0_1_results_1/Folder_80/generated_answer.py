def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(15, 20):
        if numbers[i] % 93 != 0:
            result.append(numbers[i])
    return result