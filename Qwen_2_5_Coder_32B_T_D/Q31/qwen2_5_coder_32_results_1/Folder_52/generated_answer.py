def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum_divisors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != n // i:
                    sum_divisors += n // i
        return sum_divisors == n
    return is_perfect(numbers[478]) if len(numbers) > 478 else False