def find_second_largest_num(nums):
    sliced_nums = nums[16:62]
    if len(sliced_nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sliced_nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None