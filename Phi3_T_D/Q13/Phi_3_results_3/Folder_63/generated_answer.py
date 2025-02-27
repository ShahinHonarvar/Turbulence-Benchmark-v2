def find_second_largest_num(lst):
    start, end = (max(22, 0), min(88, len(lst)))
    if start >= end:
        return None
    sub_list = lst[start:end + 1]
    unique_nums = set(sub_list)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)