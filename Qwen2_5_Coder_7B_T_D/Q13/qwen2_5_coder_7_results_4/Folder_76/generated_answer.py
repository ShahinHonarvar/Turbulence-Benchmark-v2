def find_second_largest_num(nums):
    if len(nums) < 988:
        return None
    sub_nums = nums[686:988]
    if len(sub_nums) < 2:
        return None
    largest = max(sub_nums[0], sub_nums[1])
    second_largest = min(sub_nums[0], sub_nums[1])
    for num in sub_nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest