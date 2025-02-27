def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for number in numbers:
        if number > 0:
            is_truncatable = True
            for i in range(len(str(number)) - 1):
                left_truncation = int(str(number)[i + 1:])
                right_truncation = int(str(number)[:len(str(number)) - i - 1])
                if left_truncation < 2 or right_truncation < 2:
                    is_truncatable = False
                    break
                if not is_prime(left_truncation) or not is_prime(right_truncation):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(number)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True