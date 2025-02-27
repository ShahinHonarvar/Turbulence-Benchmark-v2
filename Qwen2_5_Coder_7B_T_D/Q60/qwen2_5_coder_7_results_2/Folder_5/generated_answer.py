def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
            return False
    return True