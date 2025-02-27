def all_ints_not_div_by_num(numbers):
    result = []
    for i, num in enumerate(numbers):
        if i >= 11 and i < 56 and (num % 90 != 0):
            result.append(num)
    return result