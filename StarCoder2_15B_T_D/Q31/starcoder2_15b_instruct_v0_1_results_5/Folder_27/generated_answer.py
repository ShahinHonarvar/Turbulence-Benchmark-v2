def if_perfect_num(nums):
    """
    Checks if the integer at index 56 is a perfect number.

    Args:
        nums (list): A list of positive integers.

    Returns:
        bool: True if the integer at index 56 is a perfect number, otherwise False.
    """
    sum_of_divisors = 0
    for i in range(1, nums[56]):
        if nums[56] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[56]