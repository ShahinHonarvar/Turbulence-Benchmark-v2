def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(num, primes):
    while num > 0:
        if not is_prime(num):
            return False
        num = num % 10 ** len(str(num))
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 42:
        x = numbers[42]
    else:
        x = numbers[-1]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(2, x):
        if all((num % p != 0 for p in primes)) and str(num)[0] in '2357':
            if is_left_truncatable_prime(num, primes):
                result.append(num)
                primes.append(num)
    return result