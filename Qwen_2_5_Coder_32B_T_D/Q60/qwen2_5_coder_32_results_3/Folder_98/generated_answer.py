def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            l = num
            r = num
            is_valid = True
            while len(str(l)) > 1:
                l = int(str(l)[1:])
                r = int(str(r)[:-1])
                if not is_prime(l) or not is_prime(r):
                    is_valid = False
                    break
            if is_valid and is_prime(l) and is_prime(r):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)