def find_second_smallest_num(lst):
    start, end = (533, min(605, len(lst)))
    if end - start < 2:
        return None
    distinct_list = sorted(set(lst[start:end + 1]))
    return distinct_list[1] if len(distinct_list) > 1 else None