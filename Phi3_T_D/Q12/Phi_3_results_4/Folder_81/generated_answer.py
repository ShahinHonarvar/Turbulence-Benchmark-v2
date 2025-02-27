def find_smallest_num(numbers):
    if len(numbers) <= 100:
        return min(numbers) if numbers else None
    return min(numbers[10:101])