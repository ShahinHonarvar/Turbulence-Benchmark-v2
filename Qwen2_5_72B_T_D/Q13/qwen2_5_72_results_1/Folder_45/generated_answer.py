def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) <= 30:
        return None
    sliced_list = numbers[30:201]
    if len(sliced_list) < 2:
        return None
    max_num = max(sliced_list)
    sliced_list.remove(max_num)
    second_max = max(sliced_list) if sliced_list else None
    return second_max