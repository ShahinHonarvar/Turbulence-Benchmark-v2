def sum_of_divisors_in_range(number):

    def is_divisor(n, i):
        return n % i == 0

    def get_divisors(n):
        divisors = []
        for i in range(1, n + 1):
            if is_divisor(n, i):
                divisors.append(i)
        return divisors
    divisors = get_divisors(number)
    divisors_in_range = [d for d in divisors if 11 <= d <= 41]
    return sum(divisors_in_range)