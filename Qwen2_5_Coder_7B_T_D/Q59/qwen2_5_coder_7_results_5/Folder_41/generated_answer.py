def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        is_prime = True
        for i in str(num):
            if i == '0':
                is_prime = False
                break
            if int(str(num)[:int(i) + 1]) not in primes:
                is_prime = False
                break
        if is_prime and num not in primes:
            primes.append(num)
    return sorted(primes, reverse=True)