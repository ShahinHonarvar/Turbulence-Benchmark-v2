def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    sub_list = numbers[608:610]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]