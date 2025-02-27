def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sliced_numbers = numbers[66:94]
    if len(set(sliced_numbers)) < 2:
        return None
    return sorted(set(sliced_numbers))[-2]