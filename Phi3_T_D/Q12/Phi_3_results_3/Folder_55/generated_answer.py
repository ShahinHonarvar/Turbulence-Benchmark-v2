def find_smallest_num(numbers):
    if len(numbers) > 10:
        numbers = numbers[:10]
    return min(numbers)