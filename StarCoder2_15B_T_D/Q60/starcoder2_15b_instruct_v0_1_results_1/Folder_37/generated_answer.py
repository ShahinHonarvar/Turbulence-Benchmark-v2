def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for n in range(10, x + 1):
        if is_prime(n):
            digits = [int(d) for d in str(n)]
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(digits)):
                if not is_prime(int(''.join(map(str, digits[i:])))):
                    left_truncatable = False
                    break
            for i in range(len(digits) - 1):
                if not is_prime(int(''.join(map(str, digits[:len(digits) - i])))):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)