def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    return numbers[0] if numbers[0] < numbers[1] else numbers[1]