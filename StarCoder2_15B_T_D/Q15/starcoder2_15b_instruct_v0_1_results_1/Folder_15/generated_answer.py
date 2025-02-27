def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums[:4]:
        if num % 2 == 1:
            total += num
    return total