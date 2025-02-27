def find_second_smallest_num(numbers):
    sub_list = numbers[56:99]
    if len(sub_list) < 2:
        return 'None'
    sorted_list = sorted(set(sub_list))
    return sorted_list[1]