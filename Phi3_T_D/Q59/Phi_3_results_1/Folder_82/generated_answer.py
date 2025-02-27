def all_left_truncatable_prime(upper_bound):
    upper_bound = upper_bound[69]
    primes = [str(num) for num in range(2, upper_bound) if all((num % i for i in range(2, int(num ** 0.5) + 1)))]
    all_left_truncatable = [p for p in primes if all((is_prime(int(p[i:])) for i in range(len(p))))]
    return sorted(all_left_truncatable, reverse=True)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True