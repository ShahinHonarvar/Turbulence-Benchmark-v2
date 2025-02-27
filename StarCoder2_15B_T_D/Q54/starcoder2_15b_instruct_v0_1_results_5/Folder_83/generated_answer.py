def all_right_truncatable_prime(input):
    x = input[24]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            right_truncatable_prime = True
            for k in range(1, len(str(i))):
                if int(str(i)[k:]) % 2 == 0 or int(str(i)[k:]) % 3 == 0 or int(str(i)[k:]) % 5 == 0 or (int(str(i)[k:]) % 7 == 0):
                    right_truncatable_prime = False
                    break
            if right_truncatable_prime:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)