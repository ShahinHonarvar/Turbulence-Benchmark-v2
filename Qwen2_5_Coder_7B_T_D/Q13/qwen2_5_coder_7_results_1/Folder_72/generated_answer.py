def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[29:52]
    if len(sublist) < 2:
        return None
    largest = max(sublist[0], sublist[1])
    second_largest = min(sublist[0], sublist[1])
    for num in sublist[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None