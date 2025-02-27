def find_smallest_num(numbers):
    if len(numbers) > 9:
        numbers = numbers[:10]
    return min(numbers)