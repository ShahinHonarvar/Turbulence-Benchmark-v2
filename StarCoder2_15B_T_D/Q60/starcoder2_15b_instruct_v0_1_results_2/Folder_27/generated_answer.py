def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for num in range(11, x + 1):
        is_truncatable = True
        for i in range(1, len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True