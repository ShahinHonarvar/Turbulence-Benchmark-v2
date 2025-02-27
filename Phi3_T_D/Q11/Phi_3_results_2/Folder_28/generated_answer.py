def find_largest_num(numbers):
    try:
        return max(numbers[62:64])
    except (IndexError, ValueError):
        return None