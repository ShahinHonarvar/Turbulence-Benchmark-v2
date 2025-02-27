def find_second_smallest_num(lst):
    if len(lst[40:81]) < 2:
        return None
    sorted_slice = sorted(lst[40:81])
    return sorted_slice[1]