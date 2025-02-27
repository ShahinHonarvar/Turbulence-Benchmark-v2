def find_second_largest_num(numbers):
    if len(numbers) < 11 or not all((isinstance(x, (int, float)) for x in numbers[20:31])):
        return None
    sorted_section = sorted(numbers[20:31], reverse=True)
    return sorted_section[1] if len(sorted_section) > 1 else None