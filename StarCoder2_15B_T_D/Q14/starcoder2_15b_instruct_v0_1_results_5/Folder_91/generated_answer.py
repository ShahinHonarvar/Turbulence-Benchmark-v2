def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    for i, num in enumerate(sorted_list):
        if i >= 0 and i <= 5:
            return num
    return None