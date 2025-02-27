def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 60:
        return None
    sub_list = numbers[59:98]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]