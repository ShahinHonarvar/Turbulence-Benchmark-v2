def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[57]
    left_truncatable_primes = []
    for i in range(1, x):
        number = i
        is_left_truncatable = True
        while number > 0:
            if not is_prime(number):
                is_left_truncatable = False
                break
            number //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes