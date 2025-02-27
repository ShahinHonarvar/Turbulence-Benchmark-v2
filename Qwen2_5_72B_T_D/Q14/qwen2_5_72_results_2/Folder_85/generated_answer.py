def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sliced_numbers = numbers[:7]
    if len(sliced_numbers) < 2:
        return None
    first_smallest = min(sliced_numbers)
    sliced_numbers.remove(first_smallest)
    second_smallest = min(sliced_numbers)
    return second_smallest