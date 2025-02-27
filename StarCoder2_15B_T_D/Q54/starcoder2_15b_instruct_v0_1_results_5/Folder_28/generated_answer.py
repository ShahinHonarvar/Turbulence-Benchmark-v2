def all_right_truncatable_prime(my_tuple):
    x = my_tuple[19]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        number = i
        while number > 9:
            number //= 10
            if not is_prime(number):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True