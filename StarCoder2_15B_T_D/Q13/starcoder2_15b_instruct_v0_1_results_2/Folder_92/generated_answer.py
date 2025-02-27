def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest_num = second_largest_num = nums[0]
    for num in nums[1:]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num:
            second_largest_num = num
    return second_largest_num