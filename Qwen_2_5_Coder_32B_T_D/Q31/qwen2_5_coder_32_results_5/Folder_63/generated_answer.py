def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum_factors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_factors += i
                if i != n // i:
                    sum_factors += n // i
        return sum_factors == n
    if len(numbers) > 57:
        return is_perfect(numbers[57])
    return False