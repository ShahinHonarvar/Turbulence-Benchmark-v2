def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[250:630], start=250) if num % 850 == 0 or num % 587 == 0))