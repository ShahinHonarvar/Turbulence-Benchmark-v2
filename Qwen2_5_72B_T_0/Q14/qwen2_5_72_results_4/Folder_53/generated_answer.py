def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not 1 <= len(numbers) <= 100:
        return None
    numbers = numbers[0:101]
    numbers.sort()
    return numbers[1] if len(numbers) > 1 else None