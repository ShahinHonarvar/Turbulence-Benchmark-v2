def all_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    x = numbers[88]
    truncatables = []
    for value in range(11, x):
        str_val = str(value)
        is_truncatable = True
        if value in primes:
            for i in range(1, len(str_val)):
                if int(str_val[i:]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(value)
                truncatables.append(value)
    return sorted(truncatables)