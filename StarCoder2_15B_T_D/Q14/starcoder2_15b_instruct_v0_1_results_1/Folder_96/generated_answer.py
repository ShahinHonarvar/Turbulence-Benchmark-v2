def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) < 201:
        return None
    return sorted_list[50:201][1]