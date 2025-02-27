def find_second_smallest_num(numbers):
    if len(numbers) < 73 or len(set(numbers[31:73])) < 2:
        return None
    unique_numbers = sorted(set(numbers[31:73]))
    return unique_numbers[1]