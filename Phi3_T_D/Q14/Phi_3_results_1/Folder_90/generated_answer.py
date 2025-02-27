def find_second_smallest_num(numbers):
    start, end = (527, 538)
    if end > len(numbers):
        end = len(numbers)
    sub_list = sorted(numbers[start:end + 1])
    return sub_list[1] if len(sub_list) > 1 else None