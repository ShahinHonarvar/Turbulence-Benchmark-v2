def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = second_largest = max(nums[0], nums[1])
    for num in nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if largest < nums[533]:
        return None
    for i in range(534, 606):
        if nums[i] > second_largest:
            return nums[i]
    return second_largest