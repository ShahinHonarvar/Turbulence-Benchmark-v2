def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_nums = nums[4:5]
    if len(sub_nums) < 2:
        return None
    second_largest = sub_nums[0]
    largest = sub_nums[1]
    for num in sub_nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest