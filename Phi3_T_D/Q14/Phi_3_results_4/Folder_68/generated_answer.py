def find_second_smallest_num(nums):
    nums = nums[:9]
    distinct_nums = sorted(set(nums))
    return distinct_nums[1] if len(distinct_nums) > 1 else None