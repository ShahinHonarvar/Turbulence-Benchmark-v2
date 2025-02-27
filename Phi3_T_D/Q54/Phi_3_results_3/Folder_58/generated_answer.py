def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    truncable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            digits = list(str(num))
            while digits:
                truncated = int(''.join(digits))
                if not is_prime(truncated):
                    break
                digits.pop()
            else:
                truncable_primes.append(num)
    return truncable_primes