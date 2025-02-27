def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
        return factors
    try:
        fifth_num = numbers[56]
        return get_prime_factors(fifth_num)
    except IndexError:
        return 'Index out of range'