def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = nums[0]
    second_largest = None
    for num in nums[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num
    if second_largest is None:
        return None
    return second_largest