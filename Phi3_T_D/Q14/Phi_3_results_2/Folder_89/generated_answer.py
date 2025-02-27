def find_second_smallest_num(lst):
    try:
        target_range = lst[62:64]
        if len(target_range) < 2:
            return None
        return sorted(target_range)[1]
    except IndexError:
        return None