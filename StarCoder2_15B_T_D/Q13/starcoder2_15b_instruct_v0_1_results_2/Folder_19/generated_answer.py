def find_second_largest_num(nums):
    largest, second_largest = (float('-inf'), float('-inf'))
    for num in nums[3:6]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None