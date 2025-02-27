def find_largest_num(numbers):
    if len(numbers) <= 98 and 98 - 56 >= 0:
        return max(numbers[56:99])
    return None