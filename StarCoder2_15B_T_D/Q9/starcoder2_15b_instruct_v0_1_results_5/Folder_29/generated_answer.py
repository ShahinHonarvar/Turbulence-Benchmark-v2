def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(len(nums)):
        if i >= 59 and i <= 97 and (nums[i] % 2 != 0):
            odds.append(nums[i])
    return odds