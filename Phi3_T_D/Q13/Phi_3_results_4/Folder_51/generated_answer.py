def find_second_largest_num(lst):
    if 1 <= len(lst) <= 8 and all((isinstance(x, (int, float)) for x in lst)):
        sliced_list = lst[1:9]
        sliced_list.sort(reverse=True)
        return sliced_list[7] if len(sliced_list) == 8 else None
    return None