def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[:5]
    sub_list.sort()
    return sub_list[1]