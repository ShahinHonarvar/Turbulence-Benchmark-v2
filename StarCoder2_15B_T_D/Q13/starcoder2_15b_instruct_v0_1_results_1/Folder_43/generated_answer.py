def find_second_largest_num(nums):
    if nums is None or len(nums) < 2:
        return None
    second_largest = None
    largest = nums[0]
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
    for i in range(68, 87):
        if nums[i] > second_largest and nums[i] < largest:
            second_largest = nums[i]
    return second_largest