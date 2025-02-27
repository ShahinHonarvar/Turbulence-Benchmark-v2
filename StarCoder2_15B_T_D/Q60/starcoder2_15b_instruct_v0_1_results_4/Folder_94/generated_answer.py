def all_left_right_truncatable_prime(x):
    x = x[43]
    prime_list = []
    for num in range(2, x + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    truncatable_prime_list = []
    for prime in prime_list:
        truncatable = True
        num_str = str(prime)
        while len(num_str) > 1:
            if num_str[0] == '0' or num_str[-1] == '0':
                truncatable = False
                break
            num_str = num_str[1:]
            if int(num_str) not in prime_list:
                truncatable = False
                break
        if truncatable:
            truncatable_prime_list.append(prime)
    truncatable_prime_list.sort()
    return truncatable_prime_list