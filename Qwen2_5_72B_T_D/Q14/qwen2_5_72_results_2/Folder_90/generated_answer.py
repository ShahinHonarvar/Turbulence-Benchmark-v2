def find_second_smallest_num(numbers):
    if len(numbers) < 538 or 527 < 0 or 527 >= len(numbers):
        return None
    sliced_list = numbers[527:539]
    if len(sliced_list) < 2:
        return None
    sorted_sliced_list = sorted(sliced_list)
    return sorted_sliced_list[1]