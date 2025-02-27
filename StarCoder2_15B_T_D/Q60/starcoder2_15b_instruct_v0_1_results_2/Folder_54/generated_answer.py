def all_left_right_truncatable_prime(tup):
    x = tup[88]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            leading_digit = int(str(i)[:j])
            trailing_digit = int(str(i)[j:])
            if not is_prime(leading_digit) or not is_prime(trailing_digit):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True