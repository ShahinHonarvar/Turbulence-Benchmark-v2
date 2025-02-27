def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes_set = set()
    for num in range(2, x):
        if all((num % d for d in range(2, int(num ** 0.5) + 1))):
            primes_set.add(num)
    right_truncatable_primes = []
    for num in primes_set:
        str_num = str(num)
        while str_num:
            if int(str_num) not in primes_set:
                break
            str_num = str_num[:-1]
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)