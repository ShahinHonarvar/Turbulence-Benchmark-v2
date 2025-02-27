def find_second_smallest_num(nums):
    start = min(max(21, 0), len(nums) - 1)
    end = min(max(97, 0), len(nums) - 1)
    distinct_nums = set(nums[start:end + 1])
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[1]