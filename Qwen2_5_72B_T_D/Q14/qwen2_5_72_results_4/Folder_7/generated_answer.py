def find_second_smallest_num(numbers):
    if not 686 <= 987 < len(numbers):
        return None
    sub_list = numbers[686:988]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]