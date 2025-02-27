def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % i != 0 or int(str(i)[:len(str(i)) - j]) % i != 0:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes