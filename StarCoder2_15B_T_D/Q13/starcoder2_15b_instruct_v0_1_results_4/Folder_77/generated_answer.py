def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 539:
        return None
    second_largest = sorted_numbers[527]
    for i in range(527, 539):
        if sorted_numbers[i] > second_largest:
            second_largest = sorted_numbers[i]
    return second_largest