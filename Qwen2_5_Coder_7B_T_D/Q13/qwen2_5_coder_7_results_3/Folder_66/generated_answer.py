def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sub_list = numbers[50:55]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]