def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0 and is_prime(num):
            if is_left_right_truncatable_prime(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
            return False
    return True