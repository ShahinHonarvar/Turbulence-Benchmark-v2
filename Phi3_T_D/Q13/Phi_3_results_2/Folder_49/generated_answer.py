def find_second_largest_num(numbers):
    if 80 <= len(numbers) <= 200:
        numbers_sorted = sorted(numbers[80:201], reverse=True)
        if len(numbers_sorted) < 2:
            return None
        return numbers_sorted[1]
    return None