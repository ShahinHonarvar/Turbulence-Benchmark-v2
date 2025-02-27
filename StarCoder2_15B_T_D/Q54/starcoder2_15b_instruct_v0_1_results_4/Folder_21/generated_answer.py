def all_right_truncatable_prime(tup):
    x = tup[175]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(1, len(str(i))):
            truncated_number = int(str(i)[:-j])
            if not is_prime(truncated_number):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True