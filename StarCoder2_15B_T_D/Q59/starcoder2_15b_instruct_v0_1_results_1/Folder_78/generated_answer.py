def all_left_truncatable_prime(input_tuple):
    x = input_tuple[23]
    prime_numbers = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    left_truncatable_prime_numbers = []
    for num in prime_numbers:
        is_left_truncatable = True
        truncated_num = num
        while truncated_num > 0:
            if truncated_num % 10 == 0:
                is_left_truncatable = False
                break
            truncated_num //= 10
        if is_left_truncatable:
            left_truncatable_prime_numbers.append(num)
    return sorted(left_truncatable_prime_numbers)