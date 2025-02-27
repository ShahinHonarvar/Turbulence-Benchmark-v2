def if_perfect_num(nums):
    """
    Returns True if the integer at index 64 is a perfect number, otherwise, returns False.
    """

    def divisors(n):
        return [d for d in range(1, n) if n % d == 0]
    return sum(divisors(nums[64])) == nums[64]