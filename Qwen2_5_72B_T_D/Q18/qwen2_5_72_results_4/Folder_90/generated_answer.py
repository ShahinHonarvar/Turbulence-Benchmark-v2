def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[138:425]
    filtered_numbers = [num for num in relevant_numbers if num % -863 == 0 or num % -329 == 0]
    return sum(filtered_numbers)