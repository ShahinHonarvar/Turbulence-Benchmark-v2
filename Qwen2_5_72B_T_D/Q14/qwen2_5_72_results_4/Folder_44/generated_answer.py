def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = numbers[90:100]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]