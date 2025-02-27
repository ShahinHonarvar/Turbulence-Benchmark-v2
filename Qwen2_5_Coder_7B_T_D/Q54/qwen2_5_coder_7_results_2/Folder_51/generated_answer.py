def all_right_truncatable_prime(numbers):
    x = numbers[54]
    prime_set = set()
    for num in range(2, x):
        if all((num % d != 0 for d in range(2, int(num ** 0.5) + 1))):
            prime_set.add(num)
    right_truncatable_primes = []
    for prime in prime_set:
        is_right_truncatable = True
        for i in range(1, len(str(prime))):
            if int(str(prime)[:-i]) not in prime_set:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)