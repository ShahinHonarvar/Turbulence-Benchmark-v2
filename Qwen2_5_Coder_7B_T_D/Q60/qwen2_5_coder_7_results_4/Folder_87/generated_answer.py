def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and is_prime(num) for digit in str(num))):
            primes.append(num)
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_left_right_truncatable = True
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True