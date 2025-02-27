def if_perfect_num(nums):

    def is_perfect_num(n):
        sum_divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != 1 and i != n // i:
                    sum_divisors += n // i
        return sum_divisors == n
    return is_perfect_num(nums[85])