def find_largest_num(numbers):
    if len(numbers) <= 200:
        return max(numbers)
    return max(numbers[70:201])