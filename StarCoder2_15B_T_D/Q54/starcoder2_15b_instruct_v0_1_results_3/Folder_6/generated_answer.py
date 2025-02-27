def all_right_truncatable_prime(input_tuple):
    x = input_tuple[74]
    right_truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(1, len(str(i))):
            truncated_num = int(str(i)[:-j])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True