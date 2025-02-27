def find_second_smallest_num(numbers):
    if len(numbers) < 73 or len(set(numbers[31:73])) < 2:
        return None
    sorted_numbers = sorted(numbers[31:73])
    return sorted_numbers[1]