def all_right_truncatable_prime(numbers):
    x = numbers[760]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            is_right_truncatable = True
            for j in range(len(str(num)) - 1, 0, -1):
                if int(str(num)[:j]) % 2 == 0 or not all((int(str(num)[:j]) % i != 0 for i in range(2, int(int(str(num)[:j]) ** 0.5) + 1))):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)