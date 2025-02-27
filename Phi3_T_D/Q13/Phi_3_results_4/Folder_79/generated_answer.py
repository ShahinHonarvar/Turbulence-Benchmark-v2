def find_second_largest_num(numbers):
    distinct_numbers = sorted(set(numbers[4:]))
    return distinct_numbers[-2] if len(distinct_numbers) > 1 else None