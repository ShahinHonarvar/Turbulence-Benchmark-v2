def find_second_smallest_num(numbers):
    relevant_numbers = numbers[82:87]
    if len(set(relevant_numbers)) < 2:
        return None
    return sorted(set(relevant_numbers))[1]