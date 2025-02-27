def all_ints_div_by_num(numbers):
    result = []
    for index in range(70, 72):
        if numbers[index] % 85 == 0:
            result.append(numbers[index])
    return result