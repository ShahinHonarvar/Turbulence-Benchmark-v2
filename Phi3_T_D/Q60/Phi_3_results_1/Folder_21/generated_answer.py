def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(primes, number):
    str_num = str(number)
    for i in range(len(str_num)):
        if int(str_num[i:]) not in primes or int(str_num[:i + 1]) not in primes:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[174]
    primes = [2]
    for num in range(3, x + 1, 2):
        if is_prime(num):
            primes.append(num)
    truncatable_primes = [prime for prime in primes if is_truncatable(primes, prime)]
    return sorted(truncatable_primes)