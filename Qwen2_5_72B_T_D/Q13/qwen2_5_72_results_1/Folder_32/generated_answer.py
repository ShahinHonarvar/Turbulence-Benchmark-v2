def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(set(numbers)) != len(numbers):
        return None
    sub_list = numbers[21:98]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]