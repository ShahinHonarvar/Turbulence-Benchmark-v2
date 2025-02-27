def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    sorted_numbers = sorted(numbers[:3])
    return sorted_numbers[1] if len(set(sorted_numbers)) == len(sorted_numbers) else None