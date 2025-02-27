def all_left_truncatable_prime(numbers):
    x = numbers[8]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i))):
            if int(str(i)[j:]) % 2 == 0 or int(str(i)[j:]) % 3 == 0 or int(str(i)[j:]) % 5 == 0:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes