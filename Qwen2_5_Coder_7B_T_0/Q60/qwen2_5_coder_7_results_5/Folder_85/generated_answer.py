def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(digit) != 0 and int(str(num)[:i]) in primes and (int(str(num)[-i:]) in primes) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes)