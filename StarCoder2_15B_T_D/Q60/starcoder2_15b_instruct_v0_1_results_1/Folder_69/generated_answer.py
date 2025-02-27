def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def is_left_right_truncatable(n):
    if n < 10:
        return False
    digits = [int(d) for d in str(n)]
    while len(digits) > 1:
        if digits[0] == 0 or digits[-1] == 0 or (not is_prime[int(''.join(map(str, digits)))]):
            return False
        digits = digits[1:] + digits[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    is_prime = {i: i in sieve_of_eratosthenes(x) for i in range(x + 1)}
    truncatable = [n for n in range(x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable, reverse=True)