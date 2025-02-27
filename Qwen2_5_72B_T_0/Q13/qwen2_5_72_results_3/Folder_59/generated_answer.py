def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sliced_numbers = numbers[:10]
    if len(set(sliced_numbers)) < 2:
        return None
    largest = max(sliced_numbers)
    sliced_numbers.remove(largest)
    while largest in sliced_numbers:
        sliced_numbers.remove(largest)
    if sliced_numbers:
        return max(sliced_numbers)
    return None