def all_right_truncatable_prime(numbers):
    x = numbers[96]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            while num > 0:
                if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                    num //= 10
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)