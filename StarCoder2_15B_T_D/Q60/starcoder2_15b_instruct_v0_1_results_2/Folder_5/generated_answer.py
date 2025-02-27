def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    left_right_truncatable_primes = [2, 3, 5, 7]
    for prime in left_right_truncatable_primes:
        while len(str(prime)) > 1:
            prime = int(str(prime)[1:])
            if prime % 2 == 0 or prime % 3 == 0 or prime % 5 == 0 or (prime % 7 == 0):
                break
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)