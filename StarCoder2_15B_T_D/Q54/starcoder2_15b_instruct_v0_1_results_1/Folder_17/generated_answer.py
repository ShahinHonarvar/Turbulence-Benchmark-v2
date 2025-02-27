def all_right_truncatable_prime(tuple_positive_integers):
    right_truncatable_primes = []
    x = tuple_positive_integers[36]
    for number in tuple_positive_integers:
        if is_right_truncatable_prime(number, x):
            right_truncatable_primes.append(number)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_right_truncatable_prime(number, x):
    if number >= x:
        return False
    while number >= 10:
        if not is_prime(number):
            return False
        number //= 10
    return is_prime(number)