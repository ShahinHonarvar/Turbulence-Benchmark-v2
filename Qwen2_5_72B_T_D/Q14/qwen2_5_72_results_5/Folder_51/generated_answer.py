def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[1:9]
    if len(set(sub_list)) < 2:
        return None
    first_min = min(sub_list)
    sub_list.remove(first_min)
    second_min = min(sub_list)
    return second_min