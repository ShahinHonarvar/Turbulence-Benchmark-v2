def find_second_largest_num(distinct_nums):
    if len(distinct_nums) > 87:
        return sorted(distinct_nums[82:87])[-2] if len(set(distinct_nums[82:87])) > 1 else None
    return None