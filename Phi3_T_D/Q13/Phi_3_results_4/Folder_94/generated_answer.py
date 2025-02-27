def find_second_largest_num(numbers):
    if len(numbers) < 13:
        return 'None'
    filtered_numbers = numbers[28:41]
    if len(filtered_numbers) == 0:
        return 'None'
    unique_numbers = set(filtered_numbers)
    if len(unique_numbers) < 2:
        return 'None'
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)