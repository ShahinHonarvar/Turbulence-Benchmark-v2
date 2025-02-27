def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_truncatable_primes(limit):
    truncatable_primes = []
    try_digits = []
    last_prefix = 0
    while last_prefix < limit:
        prefix = last_prefix * 10 + 1
        while prefix <= limit:
            if is_prime(prefix):
                num_digits = len(str(prefix))
                for i in range(num_digits, 1, -1):
                    truncated_prefix = int(str(prefix)[:i])
                    if truncated_prefix != 0 and is_prime(truncated_prefix):
                        if truncated_prefix not in try_digits:
                            truncatable_primes.append(truncated_prefix)
                            try_digits.append(truncated_prefix)
            prefix += 2
        last_prefix += 1
        if len(str(last_prefix)) > 1:
            last_prefix = last_prefix % 100000000003
    return truncatable_primes

def all_right_truncatable_prime(params):
    x = params[11]
    return sorted(find_truncatable_primes(x - 1))