def find_second_largest_num(numbers):
    start_index = min(len(numbers), 40)
    end_index = min(max(start_index, 80) + 1, len(numbers))
    if start_index >= end_index:
        return None
    sliced_numbers = numbers[start_index:end_index]
    max_num = max(sliced_numbers)
    second_max_num = None
    for num in sliced_numbers:
        if num != max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num