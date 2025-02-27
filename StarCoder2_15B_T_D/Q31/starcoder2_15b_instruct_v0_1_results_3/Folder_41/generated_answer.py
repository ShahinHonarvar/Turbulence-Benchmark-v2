def if_perfect_num(nums):
    """
    This function takes a list of positive integers, and returns true if the integer at index 84 is a perfect number, otherwise, it returns false.
    """
    divisors = [i for i in range(1, nums[84]) if nums[84] % i == 0]
    return sum(divisors) == nums[84]