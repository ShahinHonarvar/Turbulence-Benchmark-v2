def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for num in nums[:7]:
        if num % 2 == 1:
            sum_odd += num
    return sum_odd