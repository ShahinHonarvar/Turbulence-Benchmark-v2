def find_second_largest_num(nums):
    nums = sorted(nums)
    second_largest = None
    for num in nums[56:58]:
        if second_largest is None or num > second_largest:
            second_largest = num
    return second_largest