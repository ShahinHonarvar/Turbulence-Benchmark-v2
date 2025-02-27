def find_second_smallest_num(nums):
    start, end = (28, min(len(nums), 41))
    second_smallest = None
    distinct_nums = {}
    for num in nums[start:end]:
        distinct_nums[num] = distinct_nums.get(num, 0) + 1
    if len(distinct_nums) < 2:
        return None
    sorted_nums = sorted(distinct_nums)
    return sorted_nums[1]