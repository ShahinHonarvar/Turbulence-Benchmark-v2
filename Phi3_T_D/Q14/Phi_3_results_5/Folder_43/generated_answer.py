def find_second_smallest_num(numbers):
    range_numbers = numbers[74:96]
    if len(range_numbers) < 2:
        return None
    distinct_numbers = sorted(set(range_numbers))
    if len(distinct_numbers) < 2:
        return None
    second_smallest = distinct_numbers[1]
    return second_smallest