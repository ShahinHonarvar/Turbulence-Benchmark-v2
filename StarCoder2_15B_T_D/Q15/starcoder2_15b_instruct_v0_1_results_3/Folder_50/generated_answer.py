def sum_odd_ints_inclusive(nums):
    total = 0
    for i, num in enumerate(nums):
        if 70 <= i <= 84 and num % 2 == 1:
            total += num
    return total