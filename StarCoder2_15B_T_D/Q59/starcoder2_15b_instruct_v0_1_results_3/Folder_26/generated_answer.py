def all_left_truncatable_prime(numbers):
    x = numbers[81]
    prime_list = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    left_truncatable_prime_list = []
    for prime in prime_list:
        is_left_truncatable_prime = True
        temp = prime
        while temp > 0:
            if temp % 10 == 0:
                is_left_truncatable_prime = False
                break
            temp //= 10
        if is_left_truncatable_prime:
            left_truncatable_prime_list.append(prime)
    return sorted(left_truncatable_prime_list, reverse=True)