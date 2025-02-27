def find_largest_num(nums):
    largest = nums[20]
    for num in nums[21:31]:
        if num > largest:
            largest = num
    return largest