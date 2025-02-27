def find_second_smallest_num(nums):
    if len(nums[1:9]) != 8:
        return None
    distinct_nums = set(nums[1:9])
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[1]