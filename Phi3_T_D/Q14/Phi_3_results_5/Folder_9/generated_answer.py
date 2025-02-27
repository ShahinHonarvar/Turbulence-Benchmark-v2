def find_second_smallest_num(num_list):
    sub_list = sorted(num_list[70:201])
    return sub_list[1] if len(sub_list) > 1 else None