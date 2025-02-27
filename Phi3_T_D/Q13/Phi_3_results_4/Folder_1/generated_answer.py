def find_second_largest_num(numbers):
    if len(numbers) < 43:
        return None
    sorted_numbers = sorted(numbers[31:73])
    return sorted_numbers[-2]