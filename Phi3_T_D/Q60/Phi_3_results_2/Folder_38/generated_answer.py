def is_prime_left_right(n, valid_lengths=[str(i) for i in range(20)]):
    str_n = str(n)
    if not all((c in '123456789' for c in str_n)):
        return False
    for len_ in valid_lengths:
        if len_ == '1':
            if int(str_n) not in (2, 3, 5, 7):
                return False
        else:
            for i in range(len_):
                sub_str_n = str_n[i:i + len_]
                if sub_str_n[0] == '0' or sub_str_n[-1] == '0':
                    return False
                if int(sub_str_n) not in (2, 3, 5, 7):
                    return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    min_digit = 2
    max_digit = min(x, 7)
    truncatable_primes = [p for p in range(min_digit, max_digit + 1) if str(p) in ['2', '3', '5', '7']]
    final_primes = []
    while truncatable_primes:
        prime = truncatable_primes[-1]
        if prime <= x:
            final_primes.append(prime)
            truncatable_primes = [p for p in truncatable_primes if is_prime_left_right(p)]
        else:
            truncatable_primes = [p for p in truncatable_primes[:-1]]
    return final_primes