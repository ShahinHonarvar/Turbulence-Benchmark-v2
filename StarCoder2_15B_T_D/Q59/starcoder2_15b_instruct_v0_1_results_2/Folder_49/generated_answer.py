def all_left_truncatable_prime(input_tuple):
    x = input_tuple[14]
    left_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            number_str = str(i)
            is_left_truncatable = True
            for k in range(len(number_str)):
                truncated_number_str = number_str[k:]
                truncated_number = int(truncated_number_str)
                for l in range(2, truncated_number):
                    if truncated_number % l == 0:
                        is_left_truncatable = False
                        break
                if not is_left_truncatable:
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes