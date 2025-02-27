def find_largest_num(numbers):
    if len(numbers) > 66:
        return max(numbers[56:67])
    elif len(numbers) > 56:
        return max(numbers[56:])
    else:
        return None