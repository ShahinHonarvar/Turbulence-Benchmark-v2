def all_left_truncatable_prime(numbers):
    x = numbers[78]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(str(num)[:i]) in primes for i in range(1, len(str(num)) + 1))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes, reverse=True)