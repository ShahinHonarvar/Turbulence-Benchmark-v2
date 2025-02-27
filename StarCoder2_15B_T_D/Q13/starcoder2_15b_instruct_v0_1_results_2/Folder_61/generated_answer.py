def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    second_largest = nums[0]
    for num in nums[1:8]:
        if num > second_largest:
            second_largest = num
    return second_largest