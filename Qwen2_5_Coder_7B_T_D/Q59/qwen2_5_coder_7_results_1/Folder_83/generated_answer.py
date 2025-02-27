def all_left_truncatable_prime(numbers):
    x = numbers[24]
    primes = []
    for num in range(2, x):
        if all((int(digit) != 0 and all((int(digit) != 0 and int(digit) % 2 != 0 for digit in str(num)[:i + 1])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)