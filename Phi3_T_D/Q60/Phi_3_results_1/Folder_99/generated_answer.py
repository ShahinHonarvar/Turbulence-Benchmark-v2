def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    truncatable_primes = []

    def is_truncatable_prime(number):
        for i in range(len(str(number))):
            if not is_prime(int(str(number)[:i + 1])):
                return False
            if not is_prime(int(str(number)[-i - 1:])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes