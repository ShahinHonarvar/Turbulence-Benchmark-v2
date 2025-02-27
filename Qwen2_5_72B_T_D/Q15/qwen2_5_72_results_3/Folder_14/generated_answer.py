def sum_odd_ints_inclusive(nums):
    relevant_numbers = nums[5:8]
    return sum((num for num in relevant_numbers if num % 2 != 0))