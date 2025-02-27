def find_second_largest_num(nums):
    second_largest = None
    for num in nums[35:50]:
        if num > second_largest or second_largest is None:
            second_largest = num
    return second_largest