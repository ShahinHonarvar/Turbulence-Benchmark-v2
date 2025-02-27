def find_second_largest_num(numbers):
    sliced_numbers = numbers[20:201]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[-2]