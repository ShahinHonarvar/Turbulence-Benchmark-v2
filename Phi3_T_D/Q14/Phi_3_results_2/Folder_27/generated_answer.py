def find_second_smallest_num(numbers):
    valid_numbers = [num for num in numbers[25:59 + 1] if isinstance(num, (int, float))]
    if len(valid_numbers) >= 2:
        valid_numbers.sort()
        return valid_numbers[1]
    return None