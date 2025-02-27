def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    second_largest = None
    for num in nums[100:201]:
        if num > second_largest or second_largest is None:
            second_largest = num
    return second_largest