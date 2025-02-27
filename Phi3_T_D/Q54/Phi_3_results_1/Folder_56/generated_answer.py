def all_right_truncatable_prime(number_tuple):
    x = number_tuple[30]
    end = ['2', '3', '5', '7']
    result_list = get_truncatable_primes(end, [], x)
    return result_list

def is_prime(n, primes):
    if n in primes:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    primes.add(n)
    return True

def get_truncatable_primes(possible_endings, primes, x):
    result = []
    for start in possible_endings:
        if int(start) > x:
            return result
        if is_prime(int(start), primes):
            primes.add(int(start))
            for tail in get_truncatable_primes(end, primes, int(start)):
                result.append(tail)
    result.append(possible_endings[0])
    return result