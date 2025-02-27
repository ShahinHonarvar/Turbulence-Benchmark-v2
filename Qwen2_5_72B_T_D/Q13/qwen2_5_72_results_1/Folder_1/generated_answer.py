def find_second_largest_num(numbers):
    if len(numbers) < 73 or len(numbers) < 32:
        return None
    sliced_numbers = numbers[31:73]
    if len(sliced_numbers) < 2:
        return None
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    second_largest = max(sliced_numbers) if sliced_numbers else None
    return second_largest