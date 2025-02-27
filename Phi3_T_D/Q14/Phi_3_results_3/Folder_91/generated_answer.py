def find_second_smallest_num(numbers):
    if len(numbers) <= 5:
        valid_numbers = numbers
    else:
        valid_numbers = numbers[:5]
    distinct_numbers = list(set(valid_numbers))
    distinct_numbers.sort()
    if len(distinct_numbers) < 2:
        return None
    else:
        return distinct_numbers[1]