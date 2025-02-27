def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(number):
    if not is_prime(number):
        return False
    number_str = str(number)
    while len(number_str) > 1:
        number_str = number_str[1:]
        if not is_prime(int(number_str)):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True