def find_second_smallest_num(numbers):
    if len(numbers) > 8:
        numbers = numbers[:8]
    sorted_numbers = sorted(numbers)
    unique_numbers = set(sorted_numbers)
    if len(unique_numbers) < 2:
        return None
    second_smallest = min(filter(lambda x: x != sorted_numbers[0], unique_numbers))
    return second_smallest