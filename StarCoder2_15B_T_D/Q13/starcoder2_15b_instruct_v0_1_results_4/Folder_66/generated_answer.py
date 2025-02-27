def find_second_largest_num(input_list):
    if len(input_list) < 55:
        return None
    sublist = input_list[50:55]
    sublist.sort(reverse=True)
    return sublist[1]