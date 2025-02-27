def all_right_truncatable_prime(numbers):
    x = numbers[85]
    prime_set = set(range(2, x))
    for i in range(2, int(x ** 0.5) + 1):
        prime_set -= set(range(i * i, x, i))
    right_truncatable_primes = [2, 3, 5, 7]
    for num in right_truncatable_primes:
        while num < x:
            num = num * 10 + 1
            if num >= x:
                break
            if all((int(num / 10 ** i) in prime_set for i in range(len(str(num))))):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)