def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    left_truncatable_primes = []

    def check_left_truncatable(num, last_digit):
        if num < x and num > 10 and is_prime(num):
            left_truncatable_primes.append(num)
            if len(str(num)) > 1 and num % 10 == last_digit:
                next_digit = int(str(num)[0]) - last_digit % 10
                check_left_truncatable(num // 10, next_digit)
    for i in range(1, 10):
        if is_prime(i) and x // 10 ** (len(str(x)) - 1) % 10 == i:
            check_left_truncatable(i * 10 ** (len(str(x)) - 1), i)
    return left_truncatable_primes