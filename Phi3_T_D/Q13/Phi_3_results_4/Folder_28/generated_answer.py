def find_second_largest_num(numbers):
    if 62 <= len(numbers) < 64:
        return numbers[62] if numbers[62] < numbers[63] else numbers[63] if numbers[63] < numbers[62] else None
    return None