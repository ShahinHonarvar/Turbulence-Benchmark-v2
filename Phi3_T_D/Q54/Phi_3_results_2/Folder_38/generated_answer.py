def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_primes_less_than(limit):

    def is_right_truncatable_prime(num, orig_num):
        while num:
            if not is_prime(num):
                return False
            num //= 10
        return True
    right_truncatable_primes = []
    for num in range(2, limit):
        if is_right_truncatable_prime(num, num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def all_right_truncatable_prime(numbers):
    x = numbers[28]
    return all_right_truncatable_primes_less_than(x)