def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    threshold = numbers[89]
    found_primes = []

    def is_truncatable(num):
        str_num = str(num)
        if not str_num.startswith('0') and (not str_num.endswith('0')):
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                    return False
        return True
    for n in range(2, threshold + 1):
        if is_prime(n) and is_truncatable(n):
            found_primes.append(n)
    return sorted(found_primes, reverse=True)