def find_second_smallest_num(lst):
    filtered_list = [x for x in lst[29:80] if isinstance(x, (int, float))]
    distinct_nums = list(set(filtered_list))
    if len(distinct_nums) < 2:
        return None
    distinct_nums.sort()
    return distinct_nums[1]