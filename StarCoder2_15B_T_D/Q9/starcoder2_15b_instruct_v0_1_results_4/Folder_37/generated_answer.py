def is_odd(num):
    return num % 2 == 1

def all_odd_ints_inclusive(nums):
    return [num for num in nums[1:6] if is_odd(num)]