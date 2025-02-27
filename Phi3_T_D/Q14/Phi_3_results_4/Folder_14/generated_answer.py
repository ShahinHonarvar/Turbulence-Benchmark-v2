def find_second_smallest_num(numbers):
    if len(numbers) < 9 or len(numbers) > 9:
        return None
    try:
        return sorted(numbers[8:9 + 1])[1]
    except IndexError:
        return None