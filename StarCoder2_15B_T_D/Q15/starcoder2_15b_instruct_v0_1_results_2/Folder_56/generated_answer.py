def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums:
        if num % 2 == 1:
            total += num
    return total