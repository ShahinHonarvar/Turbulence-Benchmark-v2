def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for i in range(23, numbers[8] + 1):
        if all((is_left_right_truncatable(i, digit) for digit in str(i))):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_left_right_truncatable(number, digit):
    if str(number).startswith(digit):
        return not digit in {'0', '2', '4', '5', '6', '8'} and is_prime(number)
    return is_prime(number)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True