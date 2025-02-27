def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    sub_list = numbers[31:35]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[-2]
    return None