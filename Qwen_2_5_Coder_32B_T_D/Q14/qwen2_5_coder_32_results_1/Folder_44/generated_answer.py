def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = numbers[91:100]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]