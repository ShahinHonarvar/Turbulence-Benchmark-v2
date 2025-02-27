def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in range(9, x, 2):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
            str_num = str(num)
            while str_num and all((int(str_num[:i]) % p != 0 for i in range(2, len(str_num) + 1) for p in primes)):
                right_truncatable_primes.append(int(str_num[:i]))
    return sorted(set(right_truncatable_primes), reverse=True)