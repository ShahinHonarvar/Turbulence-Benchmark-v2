def find_second_largest_num(nums):
    largest, second_largest = (float('-inf'), float('-inf'))
    for num in nums[:3]:
        if num > largest:
            largest, second_largest = (num, largest)
        elif num > second_largest:
            second_largest = num
    return second_largest