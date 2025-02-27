def all_left_truncatable_prime(tup):
    x = tup[3]
    primes = [2, 3, 5, 7]
    all_left_truncatable = []
    for num in range(11, x):
        if all((int(num) % 10 != 0 and int(num[:i]) in primes for i in range(1, len(num) + 1))):
            all_left_truncatable.append(int(num))
    return sorted(all_left_truncatable, reverse=True)