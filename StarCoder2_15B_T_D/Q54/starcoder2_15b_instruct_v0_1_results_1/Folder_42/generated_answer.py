def all_right_truncatable_prime(numbers):
    x = numbers[64]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        num = i
        while num > 0:
            if not is_prime(num):
                is_right_truncatable_prime = False
                break
            num //= 10
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True