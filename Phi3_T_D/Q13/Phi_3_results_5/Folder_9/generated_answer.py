def find_second_largest_num(numbers):
    valid_numbers = numbers[200:201]
    if len(valid_numbers) < 2:
        return None
    largest = max(valid_numbers)
    valid_numbers.remove(largest)
    return max(valid_numbers) if valid_numbers else None