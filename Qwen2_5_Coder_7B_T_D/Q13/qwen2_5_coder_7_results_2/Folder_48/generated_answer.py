def find_second_largest_num(nums):
    sub_nums = nums[533:606]
    if len(sub_nums) < 2:
        return None
    largest = max(sub_nums[0], sub_nums[1])
    second_largest = min(sub_nums[0], sub_nums[1])
    for num in sub_nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != largest else None