def all_left_right_truncatable_prime(numbers):
    x = numbers[67]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    right_truncatable_primes.sort(reverse=True)
    return (left_truncatable_primes, right_truncatable_primes)