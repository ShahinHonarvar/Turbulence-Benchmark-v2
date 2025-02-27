def find_second_largest_num(numbers):
    start, end = (12, 92)
    sub_list = sorted(numbers[start:end + 1], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None