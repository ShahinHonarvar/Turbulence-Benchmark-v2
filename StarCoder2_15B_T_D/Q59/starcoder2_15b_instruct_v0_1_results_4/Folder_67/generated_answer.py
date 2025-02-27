def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]

    def is_left_truncatable_prime_helper(num, prime_set):
        if num < 10:
            return num in prime_set
        return num in prime_set and is_left_truncatable_prime_helper(num % 10, prime_set)
    prime_set = set([2, 3, 5, 7])
    for i in range(11, x):
        if is_left_truncatable_prime_helper(i, prime_set):
            prime_set.add(i)
    return sorted(list(prime_set), reverse=True)