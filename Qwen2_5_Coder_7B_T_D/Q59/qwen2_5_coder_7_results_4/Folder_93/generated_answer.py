def all_left_truncatable_prime(numbers):
    x = numbers[11]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) in set([2, 3, 5, 7]) for i in range(1, len(str(num))))) and all((int(str(num)[:i]) % 2 != 0 and int(str(num)[:i]) % 3 != 0 and (int(str(num)[:i]) % 5 != 0) and (int(str(num)[:i]) % 7 != 0) and (int(str(num)[:i]) != 1) for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)