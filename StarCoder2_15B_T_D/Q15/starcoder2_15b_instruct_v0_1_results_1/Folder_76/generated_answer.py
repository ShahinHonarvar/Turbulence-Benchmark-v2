def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 686 and i <= 987 and (nums[i] % 2 != 0):
            sum += nums[i]
    return sum