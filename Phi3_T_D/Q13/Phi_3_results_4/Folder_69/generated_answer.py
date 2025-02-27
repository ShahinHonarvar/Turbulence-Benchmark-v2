def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    idx_start, idx_end = (32, 35)
    selected_numbers = numbers[idx_start:idx_end + 1]
    if len(set(selected_numbers)) < 2:
        return None
    return sorted(set(selected_numbers))[-2]