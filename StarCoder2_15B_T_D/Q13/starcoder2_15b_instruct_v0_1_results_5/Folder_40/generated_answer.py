def find_second_largest_num(nums):
    first_largest = second_largest = None
    for num in nums[:3]:
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest