def find_second_largest_num(nums):
    sublist = nums[62:100]
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
    return second_largest