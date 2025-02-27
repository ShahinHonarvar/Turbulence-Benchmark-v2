def all_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for num in range(2, x):
        if all((is_prime(int(num[-i - 1:])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True