def find_largest_num(numbers):
    if len(numbers) <= 78:
        return None
    else:
        return max(numbers[17:79])