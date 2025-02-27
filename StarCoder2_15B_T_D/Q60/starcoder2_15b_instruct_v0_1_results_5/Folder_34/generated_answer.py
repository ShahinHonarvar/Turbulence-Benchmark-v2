def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    x = x[18]
    for num in range(11, x + 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            continue
        is_truncatable = True
        for i in range(1, len(str(num))):
            left_trunc = int(str(num)[i:])
            right_trunc = int(str(num)[:i])
            if left_trunc % 2 == 0 or left_trunc % 3 == 0 or left_trunc % 5 == 0 or (left_trunc % 7 == 0):
                is_truncatable = False
                break
            if right_trunc % 2 == 0 or right_trunc % 3 == 0 or right_trunc % 5 == 0 or (right_trunc % 7 == 0):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes