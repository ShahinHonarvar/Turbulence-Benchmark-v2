def all_ints_div_by_both_two_nums(numbers):
    result = []
    for number in numbers:
        if number % 1 == 0 and number % -1 == 0:
            result.append(number)
    return result