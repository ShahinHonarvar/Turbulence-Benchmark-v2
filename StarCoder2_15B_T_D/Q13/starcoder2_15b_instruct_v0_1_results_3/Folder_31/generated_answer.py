def find_second_largest_num(nums):
    if len(nums) < 89:
        return None
    second_largest = None
    for i in range(75, 89):
        if nums[i] > second_largest or second_largest is None:
            second_largest = nums[i]
    return second_largest