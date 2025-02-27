def find_second_largest_num(numbers):
    sliced_numbers = numbers[75:86]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[-2]