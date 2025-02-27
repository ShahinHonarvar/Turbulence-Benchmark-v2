def all_left_truncatable_prime(numbers):
    x = numbers[792]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(11, x):
        if all((int(str(num)[:i]) in primes for i in range(1, len(str(num)) + 1))) and '0' not in str(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)