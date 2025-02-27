def all_left_truncatable_prime(numbers):
    x = numbers[618]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i))):
            truncated_num = int(str(i)[j:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True