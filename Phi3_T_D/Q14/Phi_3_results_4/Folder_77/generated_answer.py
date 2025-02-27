def find_second_smallest_num(lst):
    start_index = 639
    end_index = 975
    window = lst[start_index:end_index + 1]
    unique_elements = set(window)
    if len(unique_elements) < 2:
        return None
    else:
        second_min = sorted(unique_elements)[1]
        return second_min