def find_second_largest_num(lst):
    if len(lst) < 93:
        return None
    sub_list = lst[62:93]
    if len(sub_list) < 2:
        return None
    first, second = (sub_list[0], sub_list[1]) if sub_list[0] > sub_list[1] else (sub_list[1], sub_list[0])
    for num in sub_list[2:]:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != first else None