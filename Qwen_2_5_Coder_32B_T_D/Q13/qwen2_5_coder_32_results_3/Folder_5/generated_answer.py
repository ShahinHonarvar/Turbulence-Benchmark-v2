def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sub_list = numbers[8:10]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[-2]