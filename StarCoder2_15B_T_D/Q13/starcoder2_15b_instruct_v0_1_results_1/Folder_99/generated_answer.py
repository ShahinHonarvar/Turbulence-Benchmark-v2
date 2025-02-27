def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 371:
        return None
    second_largest = nums[370]
    for i in range(310, 371):
        if nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest