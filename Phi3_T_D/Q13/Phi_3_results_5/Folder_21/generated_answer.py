def find_second_largest_num(numbers):
    if len(numbers) < 347:
        return None
    relevant_numbers = numbers[639:976]
    unique_numbers = set(relevant_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)