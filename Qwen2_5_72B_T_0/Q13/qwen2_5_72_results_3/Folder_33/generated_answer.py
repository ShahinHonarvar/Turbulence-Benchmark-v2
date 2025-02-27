def find_second_largest_num(numbers):
    if len(numbers) < 774 or len(numbers) < 667:
        return None
    sub_list = numbers[667:775]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]