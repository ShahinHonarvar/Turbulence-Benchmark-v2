def find_second_smallest_num(numbers):
    if 75 <= len(numbers) <= 88:
        cut_list = numbers[75:89]
        unique_numbers = set(cut_list)
        if len(unique_numbers) >= 2:
            return sorted(unique_numbers)[1]
    return None