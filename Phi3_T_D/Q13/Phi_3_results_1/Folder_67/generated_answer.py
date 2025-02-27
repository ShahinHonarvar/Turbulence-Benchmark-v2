def find_second_largest_num(nums):
    start = 22
    end = 50
    distinct_nums = sorted(set(nums[start:end + 1]), reverse=True)
    return distinct_nums[1] if len(distinct_nums) > 1 else None