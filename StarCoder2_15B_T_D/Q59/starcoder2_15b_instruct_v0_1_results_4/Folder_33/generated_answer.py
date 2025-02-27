def all_left_truncatable_prime(numbers):
    numbers_list = list(numbers)
    x = numbers_list[945]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable_prime = True
        for j in range(len(str(i))):
            if i // 10 ** j not in [2, 3, 5, 7]:
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes