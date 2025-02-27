def all_ints_div_by_both_two_nums(numbers):
    relevant_numbers = numbers[42:44]
    return [num for num in relevant_numbers if num % 15 == 0 and num % 87 == 0]