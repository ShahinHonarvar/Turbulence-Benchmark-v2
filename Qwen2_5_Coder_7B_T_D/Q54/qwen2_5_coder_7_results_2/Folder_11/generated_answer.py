def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(2, x):
        if all((num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1))):
            if all((int(str(num)[:len(str(num)) - i]) % divisor != 0 for i in range(1, len(str(num))))) and str(num)[-1] not in '024568':
                primes.append(num)
    return sorted(primes)