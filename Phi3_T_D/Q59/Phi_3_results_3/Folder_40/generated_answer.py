def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    left_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        if all((is_prime(int(str(number)[i:])) for i in range(len(str(number))))):
            left_truncatable_primes.append(number)
    return left_truncatable_primes