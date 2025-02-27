def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    sliced_numbers = numbers[:4]
    max_num = max(sliced_numbers)
    sliced_numbers.remove(max_num)
    if len(sliced_numbers) == 0:
        return None
    second_max = max(sliced_numbers)
    return second_max