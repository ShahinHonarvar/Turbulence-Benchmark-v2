def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first = max(numbers[0], numbers[1])
    second = min(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != first else None