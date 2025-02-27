def find_second_largest_num(numbers):
    if len(numbers) < 15:
        return None
    relevant_numbers = numbers[35:50]
    if len(relevant_numbers) < 2:
        return None
    second_largest = sorted(set(relevant_numbers), reverse=True)[1]
    return second_largest