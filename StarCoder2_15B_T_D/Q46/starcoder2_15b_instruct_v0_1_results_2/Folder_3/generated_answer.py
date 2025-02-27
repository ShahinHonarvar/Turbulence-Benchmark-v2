def gcf_three_nums(nums):
    """
    Returns the greatest common factor of the elements at indices 31, 69, and 40 in a list of positive integers.
    """
    gcf = nums[31]
    for i in range(32, 70):
        gcf = gcd(gcf, nums[i])
    for i in range(41, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers.
    """
    while b != 0:
        a, b = (b, a % b)
    return a