def find_second_smallest_num(numbers):
    start, end = (43, 51)
    sliced_numbers = numbers[start:end + 1]
    if len(set(sliced_numbers)) < 2:
        return None
    return sorted(sliced_numbers)[1]