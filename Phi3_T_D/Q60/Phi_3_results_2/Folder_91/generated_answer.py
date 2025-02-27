def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    limit = input_tuple[0]
    truncatable_primes = []
    for x in range(10, limit + 1):
        if is_prime(x):
            is_truncatable = True
            str_num = str(x)
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i + 1])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(x)
    return sorted(truncatable_primes, reverse=True)