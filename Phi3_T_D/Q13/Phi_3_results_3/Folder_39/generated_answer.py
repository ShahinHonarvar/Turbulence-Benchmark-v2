def find_second_largest_num(numbers):
    sliced_list = numbers[20:31]
    unique_elements = list(set(sliced_list))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]