def find_second_largest_num(nums):
    largest = second_largest = None
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num
    return second_largest