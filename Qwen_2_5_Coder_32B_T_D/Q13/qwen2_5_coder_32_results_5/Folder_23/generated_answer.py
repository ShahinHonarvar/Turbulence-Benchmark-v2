def find_second_largest_num(nums):
    if len(nums) < 72:
        return None
    sublist = nums[52:72]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], sublist[1]) if sublist[0] > sublist[1] else (sublist[1], sublist[0])
    for num in sublist[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second