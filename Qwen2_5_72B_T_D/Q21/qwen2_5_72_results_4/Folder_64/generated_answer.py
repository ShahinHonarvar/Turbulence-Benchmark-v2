def all_ints_div_by_num(numbers):
    result = []
    if numbers and len(numbers) > 0 and (numbers[0] % 4 == 0):
        result.append(numbers[0])
    return result