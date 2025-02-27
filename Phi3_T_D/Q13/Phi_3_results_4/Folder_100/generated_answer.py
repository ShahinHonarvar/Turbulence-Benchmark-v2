def find_second_largest_num(lst):
    if 42 <= len(lst) <= 68:
        section = lst[42:69]
        if len(set(section)) < 2:
            return None
        return sorted(set(section))[-2]
    return None