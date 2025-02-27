def if_perfect_num(nums):
    """
    Checks if the number at index 16 is a perfect number.
    """
    num = nums[16]
    return num == sum((divisor for divisor in range(1, num) if num % divisor == 0))