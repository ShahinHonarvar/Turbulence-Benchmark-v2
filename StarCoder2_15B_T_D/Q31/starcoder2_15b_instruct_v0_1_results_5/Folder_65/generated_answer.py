def if_perfect_num(nums):
    """
    Returns True if the integer at index 35 is a perfect number, otherwise, returns False.
    """
    num = nums[35]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False