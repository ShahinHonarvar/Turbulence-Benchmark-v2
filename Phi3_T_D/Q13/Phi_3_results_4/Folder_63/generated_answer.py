def find_second_largest_num(num_list):
    start, end = (22, 88)
    filtered_list = num_list[start:end + 1]
    if len(set(filtered_list)) < 2:
        return None
    filtered_list.sort(reverse=True)
    return filtered_list[1]