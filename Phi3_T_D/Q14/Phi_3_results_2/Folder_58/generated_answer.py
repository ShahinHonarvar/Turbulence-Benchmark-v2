def find_second_smallest_num(numbers):
    start = 310
    end = 370
    valid_numbers = sorted(numbers[start:end + 1])
    if len(valid_numbers) < 2:
        return None
    return valid_numbers[1]