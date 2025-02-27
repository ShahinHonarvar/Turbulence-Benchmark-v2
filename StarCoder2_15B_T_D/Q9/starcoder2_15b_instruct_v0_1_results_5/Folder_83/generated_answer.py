def all_odd_ints_inclusive(nums):
    odds = []
    for num in nums:
        if num % 2 != 0:
            odds.append(num)
    return odds