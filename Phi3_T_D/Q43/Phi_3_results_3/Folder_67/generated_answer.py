def find_primes_between_indices(int_list):
    primes = [x for x in int_list[17:80] if x > 1 and all((x % i for i in range(2, int(x ** 0.5) + 1)))]
    return sorted(primes, reverse=True)