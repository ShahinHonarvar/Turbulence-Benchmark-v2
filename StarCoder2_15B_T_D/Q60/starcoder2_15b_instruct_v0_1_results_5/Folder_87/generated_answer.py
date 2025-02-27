def all_left_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[39]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            digits = list(str(i))
            is_truncatable = True
            while len(digits) > 1:
                if not is_prime(int(''.join(digits))) or not is_prime(int(''.join(digits[::-1]))):
                    is_truncatable = False
                    break
                digits = digits[1:]
                digits = digits[::-1][1:][::-1]
            if is_truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True