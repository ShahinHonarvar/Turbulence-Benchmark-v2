def all_ints_div_by_num(numbers):
    result = []
    for i, num in enumerate(numbers):
        if i >= 18 and i <= 93 and (num % -85 == 0):
            result.append(num)
    return result