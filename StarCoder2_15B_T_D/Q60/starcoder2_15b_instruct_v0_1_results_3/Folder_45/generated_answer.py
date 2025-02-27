def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i))):
            truncated_num = int(str(i)[j:])
            if truncated_num < 2 or not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True