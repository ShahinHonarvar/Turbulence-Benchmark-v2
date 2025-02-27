def sum_of_divisors_in_range(n):

    def divisors(number):
        return [i for i in range(1, number + 1) if number % i == 0]
    return sum((d for d in divisors(n) if 57 <= d <= 86))