def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[89]
    right_truncatable_primes = []
    for i in range(2, x):
        num = i
        while num >= 10:
            if not is_prime(num):
                break
            num //= 10
        if num >= 2 and is_prime(num):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes