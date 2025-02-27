def find_second_largest_num(numbers):
    try:
        if len(numbers) < 10:
            return None
        target_range = numbers[7:10]
        return sorted(target_range)[-2] if len(target_range) == 3 else None
    except TypeError:
        return None