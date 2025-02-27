def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num):
            if all((is_prime(int(str(num)[:i])) and is_prime(int(str(num)[-i:])) for i in range(1, len(str(num))))):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True