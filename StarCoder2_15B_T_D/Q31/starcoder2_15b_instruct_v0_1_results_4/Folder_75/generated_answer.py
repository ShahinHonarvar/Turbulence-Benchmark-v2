def if_perfect_num(nums):

    def is_perfect(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n
    return is_perfect(nums[80])