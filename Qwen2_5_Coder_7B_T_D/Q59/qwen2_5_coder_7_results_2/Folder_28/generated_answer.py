def all_left_truncatable_prime(numbers):
    x = numbers[19]
    primes = []
    for num in range(2, x):
        if all((int(digit) != 0 and is_prime(int(digit)) for digit in str(num))):
            truncated = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncated = False
                    break
            if truncated:
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True