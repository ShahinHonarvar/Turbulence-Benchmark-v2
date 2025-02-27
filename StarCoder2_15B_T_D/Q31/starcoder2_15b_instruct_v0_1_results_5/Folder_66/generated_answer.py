def if_perfect_num(nums):
    """
    Takes a list of positive integers and returns True if the integer at index 42 is a perfect number, otherwise False.
    """

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    num = nums[42]
    divisors = get_divisors(num)
    return sum(divisors) == num