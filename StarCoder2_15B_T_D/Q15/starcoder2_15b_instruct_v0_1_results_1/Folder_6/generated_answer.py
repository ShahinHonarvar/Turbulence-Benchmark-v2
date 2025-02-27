def sum_odd_ints_inclusive(nums):
    total_sum = 0
    for num in nums[10:67]:
        if num % 2 != 0:
            total_sum += num
    return total_sum