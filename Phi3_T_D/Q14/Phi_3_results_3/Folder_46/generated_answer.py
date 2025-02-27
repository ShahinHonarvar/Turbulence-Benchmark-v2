def find_second_smallest_num(numbers):
    numbers = numbers[12:69]
    if len(numbers) < 2:
        return None
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers) if numbers else None
    return min2