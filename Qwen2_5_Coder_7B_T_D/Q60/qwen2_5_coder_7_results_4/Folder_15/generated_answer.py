def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x + 1, 2):
        if all((int(digit) != 0 for digit in str(num))):
            if all((is_prime(int(str(num)[:i + 1])) and is_prime(int(str(num)[i + 1:])) for i in range(len(str(num)) - 1))):
                primes.append(num)
    result = [p for p in primes if is_prime(int(str(p)[:2])) and is_prime(int(str(p)[-2:]))]
    return sorted(result, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True