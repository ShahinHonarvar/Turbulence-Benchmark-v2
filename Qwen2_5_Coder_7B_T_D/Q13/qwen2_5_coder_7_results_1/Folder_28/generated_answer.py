def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sub_nums = nums[62:64]
    if len(sub_nums) < 2:
        return None
    first, second = (sub_nums[0], sub_nums[1]) if sub_nums[0] < sub_nums[1] else (sub_nums[1], sub_nums[0])
    for num in sub_nums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second