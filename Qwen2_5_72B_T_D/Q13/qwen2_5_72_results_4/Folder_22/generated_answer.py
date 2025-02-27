def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) > 201:
        return None
    sub_list = numbers[40:201]
    if len(sub_list) < 2:
        return None
    unique_sub_list = list(set(sub_list))
    unique_sub_list.sort()
    if len(unique_sub_list) < 2:
        return None
    return unique_sub_list[-2]