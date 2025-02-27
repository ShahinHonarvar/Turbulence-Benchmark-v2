def all_left_right_truncatable_prime(numbers):
    prime_list = []
    end_num, start_num = (numbers[24], 10)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime):
        str_prime = str(prime)
        if len(str_prime) == 1:
            return True
        return all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:i + 1])) for i in range(len(str_prime))))
    with_truncate = [prime for prime in range(start_num, end_num + 1) if is_prime(prime)]
    for prime in with_truncate:
        if is_truncatable_prime(prime):
            prime_list.append(prime)
    return prime_list