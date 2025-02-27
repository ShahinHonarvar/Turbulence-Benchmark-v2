def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    start, end = (15, 51)
    sliced_numbers = numbers[start:end + 1]
    sliced_numbers.sort(reverse=True)
    return sliced_numbers[1] if len(sliced_numbers) > 1 else None