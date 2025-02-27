def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    sub_list = numbers[90:91]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]