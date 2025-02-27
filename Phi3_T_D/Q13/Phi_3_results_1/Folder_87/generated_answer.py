def find_second_largest_num(numbers):
    if not 36 <= len(numbers) <= 46:
        raise ValueError('The list must contain between 36 and 46 elements')
    start, end = (36, 46)
    sorted_slice = sorted(numbers[start:end + 1], reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]