def find_second_smallest_num(numbers):
    start, end = (686, min(987, len(numbers)))
    unique_numbers = {numbers[i] for i in range(start, end + 1)}
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[1]