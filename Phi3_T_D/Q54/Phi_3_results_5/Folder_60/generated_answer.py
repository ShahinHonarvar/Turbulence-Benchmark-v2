def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[87]
    primes = ['2', '3', '5', '7']
    for num in range(10, x):
        if all((is_prime(int(num[i:])) for i in range(len(str(num))))):
            primes.append(str(num))
    return sorted([int(p) for p in primes if len(p) > 1])