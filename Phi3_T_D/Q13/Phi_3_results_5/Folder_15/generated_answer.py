def find_second_largest_num(lst):
    if len(lst) < 4 or not lst:
        return None
    sorted_lst = sorted(lst[:4], reverse=True)
    distinct_nums = sorted_set(sorted_lst)
    if len(distinct_nums) < 2:
        return None
    return distinct_nums[1]

def sorted_set(lst):
    return sorted(set(lst), reverse=True)