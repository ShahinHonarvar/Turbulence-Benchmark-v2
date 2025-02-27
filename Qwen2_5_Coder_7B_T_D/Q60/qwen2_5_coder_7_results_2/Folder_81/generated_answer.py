def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(d) != 0 for d in str(num))) and all((int(str(num)[:i]) in primes and int(str(num)[-i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted([p for p in primes if all((int(d) != 0 for d in str(p))) and all((int(str(p)[:i]) in primes and int(str(p)[-i:]) in primes for i in range(1, len(str(p)))))])