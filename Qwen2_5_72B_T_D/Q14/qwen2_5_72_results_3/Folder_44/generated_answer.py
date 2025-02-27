def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sliced_numbers = numbers[90:100]
    if len(sliced_numbers) < 2:
        return None
    smallest = min(sliced_numbers)
    sliced_numbers.remove(smallest)
    second_smallest = min(sliced_numbers)
    return second_smallest