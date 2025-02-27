def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[466]
    right_truncatable_primes = []
    for i in range(len(str(x))):
        if is_prime(int(str(x)[:len(str(x)) - i])):
            right_truncatable_primes.append(int(str(x)[:len(str(x)) - i]))
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True