def find_second_smallest_num(numbers):
    if len(numbers) < 6 or len(numbers) > 6 or (not all((isinstance(n, (int, float)) for n in numbers[50:55]))):
        return None
    sorted_sublist = sorted(numbers[50:55])
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None