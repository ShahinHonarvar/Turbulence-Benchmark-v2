def find_second_largest_num(numbers):
    if len(numbers) < 62 or 16 > 61:
        return None
    sub_list = numbers[16:62]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]