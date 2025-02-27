def find_second_largest_num(nums):
    subnums = nums[29:52]
    if len(subnums) < 2:
        return None
    first, second = (subnums[0], subnums[1]) if subnums[0] > subnums[1] else (subnums[1], subnums[0])
    for num in subnums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None