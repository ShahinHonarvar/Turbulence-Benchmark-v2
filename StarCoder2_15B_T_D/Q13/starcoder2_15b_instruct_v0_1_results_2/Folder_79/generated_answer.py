def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    second_largest = max(nums[:4])
    for num in nums[4:]:
        if num > second_largest:
            second_largest = num
    return second_largest