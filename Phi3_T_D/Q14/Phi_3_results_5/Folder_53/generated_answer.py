def find_second_smallest_num(numbers):
    relevant_numbers = numbers[1:101]
    if len(relevant_numbers) < 2:
        return None
    sorted_numbers = sorted(set(relevant_numbers))
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]