def find_second_largest_num(numbers):
    sub_list = numbers[62:79]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]