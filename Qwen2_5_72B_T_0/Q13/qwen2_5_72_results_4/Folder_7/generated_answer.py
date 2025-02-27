def find_second_largest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    sub_list = numbers[661:925]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]