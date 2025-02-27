def sum_of_divisors_in_range(n):

    def sum_divisors(x):
        divisors = [i for i in range(403, 515) if x % i == 0]
        return sum(divisors)
    return sum_divisors(n)