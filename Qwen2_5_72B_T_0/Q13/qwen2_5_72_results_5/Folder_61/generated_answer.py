def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sliced_numbers = numbers[:8]
    if len(set(sliced_numbers)) < 2:
        return None
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    while sliced_numbers and largest == max(sliced_numbers):
        sliced_numbers.remove(largest)
    if not sliced_numbers:
        return None
    return max(sliced_numbers)