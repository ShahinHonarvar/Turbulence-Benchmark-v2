def find_second_smallest_num(numbers):
    if len(numbers) < 88 or len(set(numbers[25:88])) < 2:
        return None
    relevant_numbers = sorted(numbers[25:88])
    return relevant_numbers[1]