def find_second_largest_num(numbers):
    if not 62 <= len(numbers) <= 93:
        return None
    relevant_numbers = sorted(numbers[62:93])
    distinct_numbers = list(set(relevant_numbers))
    distinct_numbers.sort()
    return distinct_numbers[-2] if len(distinct_numbers) > 1 else None