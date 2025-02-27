def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num[:i]) in primes for i in range(1, len(num)))) and all((int(num[i:]) in primes for i in range(len(num)))):
            primes.append(num)
    return sorted(primes)