def find_second_largest_num(numbers):
    start, end = (68, 86)
    filtered_numbers = numbers[start:end + 1]
    if len(set(filtered_numbers)) < 2:
        return None
    return sorted(filtered_numbers, reverse=True)[1]