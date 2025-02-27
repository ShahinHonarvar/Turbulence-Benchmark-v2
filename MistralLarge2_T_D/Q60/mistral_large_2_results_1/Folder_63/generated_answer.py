def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    digits = str(num)
    if '0' in digits:
        return False
    while len(digits) > 1:
        if not is_prime(int(digits)):
            return False
        digits = digits[1:-1]
    return is_prime(int(digits))

def all_left_right_truncatable_prime(data):
    x = data[88]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)