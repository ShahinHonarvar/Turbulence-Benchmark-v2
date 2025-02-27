def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digits_to_int(digits):
    return int(''.join(map(str, digits)))

def all_truncatable_primes_from(n):
    digits = list(map(int, str(n)))
    truncatable_primes = []
    while len(digits) > 0:
        number = digits_to_int(digits)
        if is_prime(number):
            truncatable_primes.append(number)
        else:
            break
        if len(digits) == 2:
            break
        digits.pop(0)
    return truncatable_primes

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[78]
    truncatable_primes = []
    sorted_input = sorted(input_tuple, reverse=True)
    for num in sorted_input:
        if num <= x and num > 7:
            truncatable_primes += all_truncatable_primes_from(num)
    return list(set(truncatable_primes))