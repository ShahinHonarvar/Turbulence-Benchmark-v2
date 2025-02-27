def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:j + k]) in prime_numbers for j in range(len(str(i))) for k in range(1, len(str(i)) - j + 1))):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes