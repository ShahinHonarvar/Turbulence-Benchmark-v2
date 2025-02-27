def find_second_smallest_num(numbers):
    isolated_list = numbers[17:79]
    if len(isolated_list) < 2:
        return None
    sorted_list = sorted(isolated_list)
    return sorted_list[1]