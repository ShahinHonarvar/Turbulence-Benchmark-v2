def find_second_largest_num(numbers):
    if len(numbers) < 5 or len(set(numbers[:5])) <= 1:
        return None
    sorted_numbers = sorted(numbers[:5])
    return sorted_numbers[-2]