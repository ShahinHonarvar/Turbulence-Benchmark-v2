def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    sub_list = numbers[42:69]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]