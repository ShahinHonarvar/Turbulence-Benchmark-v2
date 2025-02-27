def all_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = []
    for number in range(2, x):
        is_truncatable_prime = True
        for i in range(1, len(str(number))):
            truncated_number = int(str(number)[:-i])
            if truncated_number < 2 or not all((truncated_number % j != 0 for j in range(2, int(truncated_number ** 0.5) + 1))):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(number)
    truncatable_primes.sort()
    return truncatable_primes