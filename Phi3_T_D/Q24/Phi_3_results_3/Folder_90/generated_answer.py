def sum_of_divisors_in_range(n):

    def sum_of_divisors(n):
        divisors = [1, n]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        return divisors
    divisors = sum_of_divisors(n)
    return sum((div for div in divisors if 451 <= div <= 973))