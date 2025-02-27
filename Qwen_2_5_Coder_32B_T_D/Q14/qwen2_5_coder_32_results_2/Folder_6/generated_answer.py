def find_second_smallest_num(lst):
    if len(lst) < 80:
        return None
    sub_lst = lst[29:80]
    if len(sub_lst) < 2:
        return None
    f_min = s_min = float('inf')
    for num in sub_lst:
        if num < f_min:
            s_min = f_min
            f_min = num
        elif f_min < num < s_min:
            s_min = num
    return s_min if s_min != float('inf') else None