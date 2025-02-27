def find_second_largest_num(numbers):
    start_index, end_index = (23, 23)
    if end_index >= len(numbers):
        end_index = len(numbers) - 1
    if start_index < 0:
        start_index = 0
    sorted_subset = sorted(numbers[start_index:end_index + 1], reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]