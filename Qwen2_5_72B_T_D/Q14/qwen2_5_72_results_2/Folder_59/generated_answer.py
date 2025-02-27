def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    first_10_numbers = numbers[:10]
    first_10_numbers.sort()
    if len(first_10_numbers) < 2:
        return None
    return first_10_numbers[1]