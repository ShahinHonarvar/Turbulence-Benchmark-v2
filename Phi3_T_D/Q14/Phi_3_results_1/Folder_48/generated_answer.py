def find_second_smallest_num(numbers):
    start, end = (246, min(len(numbers), 750))
    distinct_numbers = sorted(set(numbers[start:end + 1]))
    return distinct_numbers[1] if len(distinct_numbers) > 1 else None