def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[18:53]
    filtered_numbers = [num for num in relevant_numbers if num % 15 == 0 or num % 57 == 0]
    return sum(filtered_numbers)