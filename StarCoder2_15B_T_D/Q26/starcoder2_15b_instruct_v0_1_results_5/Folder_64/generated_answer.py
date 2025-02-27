def sum_in_range(nums):
    total = 0
    for num in nums:
        if -3 <= num <= 6:
            total += num
    return total