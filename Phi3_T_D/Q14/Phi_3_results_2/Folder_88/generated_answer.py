def find_second_smallest_num(numbers):
    sliced_list = numbers[6:9]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1] if sorted_list[0] != sorted_list[1] else None