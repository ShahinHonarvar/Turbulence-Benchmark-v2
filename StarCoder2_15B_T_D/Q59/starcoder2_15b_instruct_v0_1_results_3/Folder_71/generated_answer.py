def all_left_truncatable_prime(numbers):
    x = numbers[22]

    def is_truncatable_prime(num):
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
    truncatable_primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_truncatable_prime(num):
                break
            num //= 10
        else:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes