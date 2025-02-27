def find_second_largest_num(number_list):
    relevant_list = number_list[15:40]
    unique_numbers = set(relevant_list)
    if len(unique_numbers) < 2:
        return None
    largest = max(unique_numbers)
    unique_numbers.remove(largest)
    second_largest = max(unique_numbers)
    return second_largest