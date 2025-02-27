def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x):
        if all((int(num[:i]) for i in range(1, len(str(num))) if is_prime(int(num[:i])))) and is_prime(num) and ('0' not in str(num)):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True