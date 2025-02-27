def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    filtered_numbers = numbers[1:9]
    if len(set(filtered_numbers)) < 2:
        return None
    return sorted(filtered_numbers)[1]