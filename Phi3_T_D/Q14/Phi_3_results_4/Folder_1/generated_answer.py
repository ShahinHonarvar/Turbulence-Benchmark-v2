def find_second_smallest_num(lst):
    selection = lst[34:55]
    sorted_selection = sorted(selection)
    return sorted_selection[1] if len(sorted_selection) > 1 else None