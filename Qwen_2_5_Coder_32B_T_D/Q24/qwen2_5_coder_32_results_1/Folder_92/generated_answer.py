def sum_of_divisors_in_range(n):

    def divisors(x):
        return [i for i in range(1, x + 1) if x % i == 0]
    d = divisors(n)
    return sum([i for i in d if 8 <= i <= 9])