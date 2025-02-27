def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)