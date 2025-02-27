def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[0:6]:
        if num > largest:
            largest = num
    return largest