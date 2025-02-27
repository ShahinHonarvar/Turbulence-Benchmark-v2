def all_left_truncatable_prime(numbers):
    if len(numbers) < 31:
        return []
    x = numbers[30]
    left_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        number_str = str(i)
        for k in range(len(number_str)):
            truncated_number = int(number_str[k:])
            is_truncated_prime = True
            for j in range(2, truncated_number):
                if truncated_number % j == 0:
                    is_truncated_prime = False
                    break
            if not is_truncated_prime:
                break
        if is_truncated_prime:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes