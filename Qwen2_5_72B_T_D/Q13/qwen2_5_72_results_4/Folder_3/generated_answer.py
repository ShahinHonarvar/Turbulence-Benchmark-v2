def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 93:
        return None
    sub_list = numbers[62:93]
    if len(sub_list) < 2:
        return None
    unique_sub_list = list(set(sub_list))
    unique_sub_list.sort()
    if len(unique_sub_list) < 2:
        return None
    return unique_sub_list[-2]