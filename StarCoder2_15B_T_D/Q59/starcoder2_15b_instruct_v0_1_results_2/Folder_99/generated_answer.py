def all_left_truncatable_prime(input_tuple):
    x = input_tuple[758]

    def is_truncatable_prime(num, prime_set):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if int(num_str[i:]) not in prime_set:
                return False
        return True
    prime_set = set()
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_set.add(i)
    result = [prime for prime in prime_set if is_truncatable_prime(prime, prime_set)]
    result.sort()
    return result