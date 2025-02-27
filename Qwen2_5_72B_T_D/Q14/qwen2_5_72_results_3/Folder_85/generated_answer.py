def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sliced_numbers = numbers[:7]
    smallest = min(sliced_numbers)
    sliced_numbers.remove(smallest)
    if sliced_numbers:
        return min(sliced_numbers)
    else:
        return None