def find_second_largest_num(nums):
    second_largest = None
    for num in nums[1:6]:
        if num > second_largest:
            second_largest = num
    return second_largest