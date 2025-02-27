def find_second_smallest_num(numbers):
    sub_list = numbers[310:371]
    if len(sub_list) < 2:
        return None
    sub_list.remove(min(sub_list))
    return min(sub_list)