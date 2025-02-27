def find_second_largest_num(numbers):
    if len(numbers) < 538:
        return None
    sliced_numbers = numbers[527:539]
    if len(sliced_numbers) < 2:
        return None
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    second_largest = max(sliced_numbers) if sliced_numbers else None
    return second_largest