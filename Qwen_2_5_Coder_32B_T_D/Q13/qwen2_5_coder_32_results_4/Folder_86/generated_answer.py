def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    sub_list = numbers[31:35]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]