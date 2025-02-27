def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[92]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        original_num = num
        while num > 0:
            if not is_prime(num):
                break
            num = int(str(num)[1:-1] or '0')
        else:
            truncatable_primes.append(original_num)
    return sorted(truncatable_primes)