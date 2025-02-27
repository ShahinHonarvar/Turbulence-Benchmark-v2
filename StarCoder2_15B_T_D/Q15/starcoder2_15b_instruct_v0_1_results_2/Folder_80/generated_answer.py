def sum_odd_ints_inclusive(nums):
    sum_odds = 0
    for i in range(64, 67):
        if nums[i] % 2 == 1:
            sum_odds += nums[i]
    return sum_odds