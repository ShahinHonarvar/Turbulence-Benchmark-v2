def find_second_largest_num(numbers):
    if len(numbers) < 73 or len(numbers) < 32:
        return None
    sub_list = numbers[31:73]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]