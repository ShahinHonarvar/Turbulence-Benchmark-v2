def find_second_smallest_num(numbers):
    if len(numbers) < 89 or len(set(numbers[22:89])) < 2:
        return None
    sub_list = numbers[22:89]
    sub_list.sort()
    return sub_list[1]