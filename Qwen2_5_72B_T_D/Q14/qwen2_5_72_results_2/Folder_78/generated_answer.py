def find_second_smallest_num(numbers):
    if len(numbers) < 78 or len(numbers) < 17:
        return None
    sliced_list = numbers[17:79]
    if len(sliced_list) < 2:
        return None
    first_smallest = min(sliced_list)
    sliced_list.remove(first_smallest)
    second_smallest = min(sliced_list)
    return second_smallest