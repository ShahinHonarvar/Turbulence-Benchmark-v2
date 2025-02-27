def all_left_right_truncatable_prime(numbers):
    limit = numbers[54]
    truncatable_primes = []
    for n in range(11, limit + 1):
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes

def is_truncatable_prime(number):
    str_num = str(number)
    if any((digit == '0' or digit == '2' or digit == '4' or (digit == '5') or (digit == '6') or (digit == '8') for digit in str_num)):
        return False
    for i in range(1, len(str_num)):
        if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i]))):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True