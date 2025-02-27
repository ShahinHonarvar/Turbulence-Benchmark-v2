def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[78:82] if num % 76 == 0 or num % 60 == 0))