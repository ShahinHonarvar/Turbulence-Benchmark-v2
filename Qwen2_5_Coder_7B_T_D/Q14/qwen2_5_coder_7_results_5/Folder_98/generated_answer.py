def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sub_list = numbers[6:7]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]