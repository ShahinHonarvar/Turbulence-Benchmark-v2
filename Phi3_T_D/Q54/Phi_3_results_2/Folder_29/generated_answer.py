def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[55]
    right_truncatable_primes = []
    for number in range(7, x, 2):
        num_str = str(number)
        if is_prime(number):
            truncate = num_str[:-1]
            while truncate:
                if not is_prime(int(truncate)):
                    break
                truncate = truncate[:-1]
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)