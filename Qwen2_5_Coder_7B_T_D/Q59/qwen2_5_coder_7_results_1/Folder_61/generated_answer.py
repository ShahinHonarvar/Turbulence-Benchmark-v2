def all_left_truncatable_prime(numbers):
    x = numbers[3]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num[:i]) in primes for i in range(1, len(num) + 1))):
            primes.append(num)
    return sorted([p for p in primes if '0' not in str(p)], reverse=True)