def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    sub_list = numbers[91:100]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]