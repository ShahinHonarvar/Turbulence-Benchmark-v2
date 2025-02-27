def find_second_largest_num(nums):
    sub_list = nums[27:56]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    second_largest = max((num for num in sub_list if num != largest))
    return second_largest