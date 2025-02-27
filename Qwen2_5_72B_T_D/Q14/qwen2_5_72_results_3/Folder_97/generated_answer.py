def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    sub_list = numbers[31:35]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]