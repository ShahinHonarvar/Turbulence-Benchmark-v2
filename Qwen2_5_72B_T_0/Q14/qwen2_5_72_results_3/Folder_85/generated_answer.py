def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sliced_numbers = numbers[:7]
    if len(set(sliced_numbers)) < 2:
        return None
    return sorted(sliced_numbers)[1]