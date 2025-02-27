def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[54:80]
    filtered_numbers = [num for num in relevant_numbers if num % 54 == 0 or num % 28 == 0]
    return sum(filtered_numbers)