def all_left_truncatable_prime(numbers):
    x = numbers[69]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        num_str = str(i)
        for j in range(len(num_str)):
            truncated_num = int(num_str[j:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True