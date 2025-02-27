def find_second_largest_num(numbers):
    if 29 <= len(numbers) <= 93:
        return sorted(numbers[29:94], reverse=True)[1]
    return None