def all_right_truncatable_prime(numbers):
    x = numbers[645]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_right_truncatable_prime(num):
                break
            num //= 10
        if num == 0:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes