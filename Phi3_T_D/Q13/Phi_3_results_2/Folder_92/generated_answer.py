def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[:2])
    return next((num for num in numbers[:2] if num != max_num), None)