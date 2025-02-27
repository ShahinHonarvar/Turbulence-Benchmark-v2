def all_left_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for num in range(2, x):
        if all((num % d != 0 for d in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            is_truncatable = True
            for i in range(1, len(str(num))):
                if not all(int((str(num)[i:] % d != 0 for d in range(2, int(int(str(num)[i:]) ** 0.5) + 1)))):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)