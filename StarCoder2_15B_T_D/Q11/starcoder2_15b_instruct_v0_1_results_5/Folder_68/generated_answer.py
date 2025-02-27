def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[:9]:
        if num > largest:
            largest = num
    return largest