def find_second_smallest_num(numbers):
    sub_list = numbers[70:85]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1] if sorted_list[0] != sorted_list[1] else sorted_list[2]