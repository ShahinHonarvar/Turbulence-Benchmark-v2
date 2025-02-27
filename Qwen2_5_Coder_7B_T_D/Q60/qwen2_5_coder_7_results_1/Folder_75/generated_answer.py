def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num):
            if is_left_right_truncatable_prime(num):
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:i + 1])):
            return False
    return True