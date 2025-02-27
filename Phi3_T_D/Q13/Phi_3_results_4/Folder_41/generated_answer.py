def find_second_largest_num(numbers):
    relevant_numbers = numbers[6:7]
    if len(relevant_numbers) == 1:
        return None
    sorted_numbers = sorted(relevant_numbers, reverse=True)
    return sorted_numbers[1]