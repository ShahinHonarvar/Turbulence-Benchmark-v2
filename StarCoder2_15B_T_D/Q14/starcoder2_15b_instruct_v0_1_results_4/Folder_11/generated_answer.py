def find_second_smallest_num(my_list):
    my_list.sort()
    if len(my_list) >= 94:
        return my_list[67]
    else:
        return None