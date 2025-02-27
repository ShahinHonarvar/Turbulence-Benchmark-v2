def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(472, 827):
        if numbers[i] % 602 != 0:
            result.append(numbers[i])
    return result