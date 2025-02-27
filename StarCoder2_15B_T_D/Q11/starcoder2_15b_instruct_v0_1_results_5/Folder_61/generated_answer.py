def find_largest_num(nums):
    largest = nums[0]
    for num in nums[1:8]:
        if num > largest:
            largest = num
    return largest