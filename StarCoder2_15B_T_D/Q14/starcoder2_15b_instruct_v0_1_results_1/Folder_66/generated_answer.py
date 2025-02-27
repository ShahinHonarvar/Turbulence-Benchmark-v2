def find_second_smallest_num(input_list):
    if len(input_list) >= 100:
        sublist = input_list[62:100]
        sublist.sort()
        if len(sublist) >= 2:
            return sublist[1]
    return None