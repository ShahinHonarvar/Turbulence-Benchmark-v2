def sum_odd_ints_inclusive(nums):
    total = sum((num for num in nums[42:69] if num % 2 != 0))
    return total