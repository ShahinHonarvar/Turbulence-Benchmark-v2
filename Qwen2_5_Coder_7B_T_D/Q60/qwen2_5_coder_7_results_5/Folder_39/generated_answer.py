def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(digit) != 0 and all((int(digit) % i != 0 for i in range(2, int(digit) + 1))) for digit in str(num))):
            primes.append(num)
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_left_right_truncatable = True
        for i in range(len(str_prime)):
            if not all((int(str_prime[j:i + 1]) % j != 0 for j in range(2, int(str_prime[j:i + 1]) + 1))) or int(str_prime[j:i + 1]) in [0, 1]:
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)