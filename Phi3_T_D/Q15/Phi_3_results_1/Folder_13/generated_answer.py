def sum_odd_ints_inclusive(nums):
    sum_of_odds = sum((num for num in nums[25:88] if num % 2 != 0))
    return sum_of_odds