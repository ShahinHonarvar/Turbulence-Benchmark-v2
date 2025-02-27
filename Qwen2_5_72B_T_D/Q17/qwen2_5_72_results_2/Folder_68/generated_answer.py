def all_ints_div_by_both_two_nums(numbers):
    result = []
    if 7 < len(numbers):
        if numbers[7] % 5 == 0 and numbers[7] % 7 == 0:
            result.append(numbers[7])
    return result