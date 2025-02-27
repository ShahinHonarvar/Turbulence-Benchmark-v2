def find_second_largest_num(numbers):
    start, end = (34, 55)
    valid_numbers = sorted(numbers[start:end + 1], reverse=True)
    if len(valid_numbers) >= 2:
        return valid_numbers[1]
    return None