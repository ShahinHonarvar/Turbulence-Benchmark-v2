def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    number = numbers[537]
    factors = set()
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0 and is_prime(num):
            factors.add(num)
            while number % num == 0:
                number //= num
    if number > 1 and is_prime(number):
        factors.add(number)
    return factors