def find_second_largest_num(lst):
    start, end = (90, min(90 + 1, len(lst)))
    distinct_nums = set(lst[start:end])
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[-2]