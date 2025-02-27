def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[1:6]
    sub_list.sort()
    return sub_list[1]