def find_second_smallest_num(numbers):
    sub_list = numbers[80:201]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(set(sub_list))
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]