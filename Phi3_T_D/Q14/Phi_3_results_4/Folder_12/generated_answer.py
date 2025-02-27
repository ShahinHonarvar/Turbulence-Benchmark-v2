def find_second_smallest_num(lst):
    if len(lst[31:73]) < 2:
        return None
    sorted_sublist = sorted(lst[31:73])[:2]
    return sorted_sublist[1] if sorted_sublist[0] != min(lst[31:73]) else None