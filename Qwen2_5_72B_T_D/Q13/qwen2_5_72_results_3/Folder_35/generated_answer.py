def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    sliced_numbers = numbers[30:49]
    if len(set(sliced_numbers)) < 2:
        return None
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    second_largest = max(sliced_numbers)
    return second_largest