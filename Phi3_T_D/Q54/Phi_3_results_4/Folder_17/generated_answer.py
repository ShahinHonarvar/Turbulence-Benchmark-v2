def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not is_prime(int(str_n[i - 1:])):
                return False
            if len(str_n) == 1:
                if primes and int(str_n) not in primes:
                    return False
        return True
    for num in range(2, x):
        primes = []
        if all((is_prime(i) for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_right_truncatable_prime(num, primes):
                    break
                primes.add(int(str_num[i:]))
        elif is_right_truncatable_prime(num, primes):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)