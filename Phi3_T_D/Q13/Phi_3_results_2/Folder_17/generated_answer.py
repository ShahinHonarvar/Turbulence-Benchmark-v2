def find_second_largest_num(numbers):
    if 62 <= len(numbers) <= 78:
        sorted_numbers = sorted(numbers[62:79], reverse=True)
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    else:
        return None