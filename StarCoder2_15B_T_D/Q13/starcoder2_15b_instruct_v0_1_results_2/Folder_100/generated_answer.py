def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) > 69:
        second_largest = sorted_numbers[42]
    elif len(sorted_numbers) > 42:
        second_largest = sorted_numbers[1]
    else:
        second_largest = None
    return second_largest