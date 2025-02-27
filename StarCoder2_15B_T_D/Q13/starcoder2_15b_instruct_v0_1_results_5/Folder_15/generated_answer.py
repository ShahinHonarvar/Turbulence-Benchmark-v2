def find_second_largest_num(nums):
    second_largest = None
    largest = float('-inf')
    for num in nums[:4]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest