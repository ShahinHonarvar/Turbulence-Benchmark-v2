def all_right_truncatable_prime(input_tuple):
    x = input_tuple[39]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

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