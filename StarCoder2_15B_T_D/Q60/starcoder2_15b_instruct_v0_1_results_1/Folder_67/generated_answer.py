def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[71]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            digits = str(i)
            truncatable = True
            for j in range(len(digits)):
                if not is_prime(int(digits[j:])) or not is_prime(int(digits[:len(digits) - j])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)