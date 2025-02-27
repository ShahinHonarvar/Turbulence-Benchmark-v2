def all_left_right_truncatable_prime(numbers):
    x = numbers[93]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(num) % 2 != 0 and int(num) % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))):
            primes.append(num)
    left_right_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if all((int(str_prime[:i]) % 2 != 0 and int(str_prime[:i]) % i != 0 for i in range(1, len(str_prime)))):
            if all((int(str_prime[-i:]) % 2 != 0 and int(str_prime[-i:]) % i != 0 for i in range(1, len(str_prime)))):
                left_right_truncatable.append(prime)
    return sorted(left_right_truncatable)