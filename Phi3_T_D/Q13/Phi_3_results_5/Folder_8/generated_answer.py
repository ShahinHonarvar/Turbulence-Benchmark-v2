def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None
    return sorted(numbers[23:24])[-1]