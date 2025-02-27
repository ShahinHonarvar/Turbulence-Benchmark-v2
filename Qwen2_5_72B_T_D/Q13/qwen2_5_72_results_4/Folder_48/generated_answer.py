def find_second_largest_num(numbers):
    if len(numbers) < 606 or len(numbers) < 534:
        return None
    sub_list = numbers[533:606]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]