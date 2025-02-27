def all_right_truncatable_prime(numbers):
    x = numbers[61]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    for num in range(10, x):
        if is_prime(num) and is_right_truncatable(num):
            primes.append(num)
    primes.sort()
    return primes