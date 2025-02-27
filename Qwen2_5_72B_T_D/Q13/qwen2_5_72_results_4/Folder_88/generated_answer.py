def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[4:9]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]