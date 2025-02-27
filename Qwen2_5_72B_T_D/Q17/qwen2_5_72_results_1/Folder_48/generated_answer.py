def all_ints_div_by_both_two_nums(numbers):
    result = [num for num in numbers[306:958] if num % 982 == 0 and num % 319 == 0]
    return result