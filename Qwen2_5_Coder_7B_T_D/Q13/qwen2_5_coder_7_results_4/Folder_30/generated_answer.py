def find_second_largest_num(nums):
    sub_nums = nums[55:99]
    if len(sub_nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None