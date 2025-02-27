def find_second_largest_num(numbers):
    if len(numbers) < 976 or len(numbers) > 976 or len(set(numbers[639:976])) != 337:
        return None
    sliced_numbers = numbers[639:976]
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    second_largest = max(sliced_numbers) if sliced_numbers else None
    return second_largest