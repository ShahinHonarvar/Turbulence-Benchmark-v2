def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x):
        if all((int(digit) != 0 for digit in str(num))) and all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True