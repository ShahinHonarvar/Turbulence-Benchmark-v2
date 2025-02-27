def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num, prefixes, suffixes, right_to_left=True):
    str_num = str(num)
    for prefix in prefixes:
        if prefix and (not is_prime(int(prefix))):
            return False
    if right_to_left:
        for suffix in suffixes:
            if suffix == str_num:
                continue
            if not is_prime(int(suffix)):
                return False
    else:
        str_num = str_num[1:]
        for prefix in prefixes:
            if prefix and (not is_prime(int(prefix))):
                return False
        for suffix in suffixes:
            if suffix and (not is_prime(int(suffix))):
                return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    truncatable_primes = []
    for num in range(7, x + 1):
        prefixes = [str(num)[i:] for i in range(len(str(num)))]
        suffixes = [str(num)[:i] for i in range(len(str(num)), 0, -1)]
        if is_truncatable_prime(num, prefixes, suffixes):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)