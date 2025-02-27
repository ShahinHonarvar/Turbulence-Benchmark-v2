def sum_of_divisors_in_range(n):

    def divisors(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.extend([i, num // i])
        divisors = list(set(divisors))
        return sorted(divisors)
    divisors_n = divisors(n)
    divisors_in_range = [x for x in divisors_n if 403 <= x <= 514]
    return sum(divisors_in_range)