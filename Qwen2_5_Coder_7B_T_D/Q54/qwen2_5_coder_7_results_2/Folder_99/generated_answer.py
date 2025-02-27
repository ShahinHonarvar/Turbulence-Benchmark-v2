def all_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in range(11, x):
        if all((int(num[-i - 1:]) in primes for i in range(len(num)))):
            right_truncatable_primes.append(int(num))
    return sorted(right_truncatable_primes)