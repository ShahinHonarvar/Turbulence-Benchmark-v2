def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    for num in range(max(primes[-1] + 1, numbers[57]), x + 1):
        if all((num % p != 0 for p in primes)):
            primes.append(num)

    def is_truncatable(n, primes):
        str_n = str(n)
        return all((int(str_n[i:]) in primes for i in range(len(str_n))))
    left_right_primes = [p for p in primes if is_truncatable(p, primes)]
    left_right_primes.sort(reverse=True)
    return left_right_primes