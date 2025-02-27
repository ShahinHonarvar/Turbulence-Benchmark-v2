def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(11, x):
        if all((int(digit) != 0 for digit in str(num))) and all((int(str(num)[:i]) in primes for i in range(1, len(str(num)) + 1))):
            left_truncatable_primes.append(num)
            primes.extend([int(str(num)[:i]) for i in range(1, len(str(num)) + 1) if int(str(num)[:i]) not in primes])
    return sorted(left_truncatable_primes, reverse=True)