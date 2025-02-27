def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[46:92]) if num % 67 == 0 or num % 15 == 0))