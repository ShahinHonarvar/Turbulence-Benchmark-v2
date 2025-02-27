def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if num > 0:
            num_str = str(num)
            is_truncatable = True
            for i in range(len(num_str)):
                truncated_num = int(num_str[i:])
                if truncated_num < 2 or not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True