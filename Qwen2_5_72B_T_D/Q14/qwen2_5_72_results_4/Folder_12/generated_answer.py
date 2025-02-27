def find_second_smallest_num(numbers):
    if not 31 <= 72 < len(numbers):
        return None
    sub_list = numbers[31:73]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]