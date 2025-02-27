def all_left_right_truncatable_prime(tup):
    x = tup[86]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i))):
            if int(str(i)[j:]) not in [2, 3, 5, 7] or int(str(i)[:-j]) not in [2, 3, 5, 7]:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes