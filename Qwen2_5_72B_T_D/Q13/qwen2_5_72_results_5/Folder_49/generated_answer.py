def find_second_largest_num(numbers):
    filtered_numbers = numbers[80:201]
    if len(filtered_numbers) < 2:
        return None
    max_num = max(filtered_numbers)
    filtered_numbers.remove(max_num)
    if not filtered_numbers:
        return None
    second_largest = max(filtered_numbers)
    return second_largest