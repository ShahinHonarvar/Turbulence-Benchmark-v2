def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]