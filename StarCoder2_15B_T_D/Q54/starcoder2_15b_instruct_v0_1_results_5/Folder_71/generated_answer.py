def all_right_truncatable_prime(input_tuple):
    x = input_tuple[22]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        for i in range(len(str(num)) - 1):
            truncated_num = int(str(num)[:-i - 1])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True