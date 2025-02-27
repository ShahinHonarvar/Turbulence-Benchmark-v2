def sum_odd_ints_inclusive(nums):
    odd_ints = [num for num in nums[1:2] if num % 2 == 1]
    return sum(odd_ints) if odd_ints else 0