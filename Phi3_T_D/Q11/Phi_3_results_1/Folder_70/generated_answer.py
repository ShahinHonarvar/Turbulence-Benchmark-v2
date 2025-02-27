def find_largest_num(numbers):
    if len(numbers) > 32:
        return max(numbers[28:33])
    else:
        return None