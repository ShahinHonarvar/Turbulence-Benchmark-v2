def find_second_smallest_num(numbers):
    sub_list = numbers[15:40]
    if len(sub_list) < 2:
        return None
    sorted_subset = sorted(sub_list)
    return sorted_subset[1]