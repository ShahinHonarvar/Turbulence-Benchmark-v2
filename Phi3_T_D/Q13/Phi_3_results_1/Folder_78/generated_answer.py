def find_second_largest_num(numbers):
    start = 43
    end = 51
    specific_values = numbers[start:end + 1]
    if len(specific_values) < 2:
        return None
    sorted_values = sorted(specific_values)
    return sorted_values[-2]