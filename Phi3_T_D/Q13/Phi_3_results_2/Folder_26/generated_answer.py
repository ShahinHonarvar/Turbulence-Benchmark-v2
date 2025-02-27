def find_second_largest_num(numbers):
    relevant_numbers = numbers[62:100]
    if len(set(relevant_numbers)) < 2:
        return None
    sorted_numbers = sorted(relevant_numbers, reverse=True)
    second_largest = sorted_numbers[1]
    return second_largest