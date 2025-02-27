def find_second_largest_num(num_list):
    if not 75 <= len(num_list) <= 88:
        return None
    return sorted(num_list[75:89])[-2]