def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    sliced_list = numbers[20:31]
    if len(sliced_list) < 2:
        return None
    first_smallest = min(sliced_list)
    sliced_list.remove(first_smallest)
    second_smallest = min(sliced_list)
    return second_smallest