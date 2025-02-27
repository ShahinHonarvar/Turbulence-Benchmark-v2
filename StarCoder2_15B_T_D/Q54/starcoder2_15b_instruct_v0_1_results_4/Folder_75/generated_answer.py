def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            right_truncatable_prime = True
            for k in range(1, len(str(i))):
                truncated_number = int(str(i)[:-k])
                if truncated_number < 2:
                    right_truncatable_prime = False
                    break
                for j in range(2, truncated_number):
                    if truncated_number % j == 0:
                        right_truncatable_prime = False
                        break
            if right_truncatable_prime:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes