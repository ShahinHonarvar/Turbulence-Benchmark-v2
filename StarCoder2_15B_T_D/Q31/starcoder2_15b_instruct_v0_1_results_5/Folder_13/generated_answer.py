def if_perfect_num(nums):
    """
    This function takes a list of positive integers and returns True if the integer at index 126 is a perfect number, otherwise it returns False.
    """

    def is_perfect(n):
        return sum([i for i in range(1, n) if n % i == 0]) == n
    return is_perfect(nums[126])