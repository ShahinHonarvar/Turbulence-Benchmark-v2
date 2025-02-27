def all_right_truncatable_prime(input_tuple):
    x = input_tuple[6]
    right_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            number_str = str(i)
            for k in range(len(number_str) - 1, 0, -1):
                truncated_number = int(number_str[:k])
                is_truncated_prime = True
                for j in range(2, truncated_number):
                    if truncated_number % j == 0:
                        is_truncated_prime = False
                        break
                if not is_truncated_prime:
                    is_prime = False
                    break
            if is_prime:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes