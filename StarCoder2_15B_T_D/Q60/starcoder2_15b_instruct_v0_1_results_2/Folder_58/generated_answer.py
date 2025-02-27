def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if int(num_str[i:]) not in truncatable_primes:
                return False
            if int(num_str[:i + 1]) not in truncatable_primes:
                return False
        return True
    truncatable_primes = [2, 3, 5, 7, 13, 17, 31, 37, 71, 73, 79, 97]
    x = numbers[975]
    return sorted([prime for prime in truncatable_primes if prime <= x and is_truncatable_prime(prime)], reverse=True)