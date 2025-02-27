def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num):
            if is_left_right_truncatable(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i - 1])):
            return False
    return True