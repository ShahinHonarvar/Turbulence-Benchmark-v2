def all_left_truncatable_prime(numbers):
    x = numbers[57]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x):
        if all((int(num) % 10 != 0 and is_prime(int(num)) for num in str(num))):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True