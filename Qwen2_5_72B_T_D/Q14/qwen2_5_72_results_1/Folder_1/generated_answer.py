def find_second_smallest_num(numbers):
    if len(numbers) < 56 or len(set(numbers)) != len(numbers):
        return None
    sub_list = numbers[34:56]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]