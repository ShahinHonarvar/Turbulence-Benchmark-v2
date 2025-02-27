def if_perfect_num(nums):
    """
    Write a function called 'if_perfect_num' takes one argument, a list of positive integers,
    and returns true if the integer at index 851 is a perfect number, otherwise, it should return false.
    """

    def divisors(n):
        return [i for i in range(1, n) if n % i == 0]
    if divisors(nums[851]) == [i for i in range(1, 851) if 851 % i == 0]:
        return True
    else:
        return False