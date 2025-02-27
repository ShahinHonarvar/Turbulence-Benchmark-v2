def find_second_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 71:
        return None
    sub_list = numbers[70:85]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]