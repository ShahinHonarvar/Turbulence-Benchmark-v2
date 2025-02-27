def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[466]

    def is_truncatable_prime(num):
        if num in [2, 3, 5, 7]:
            return True
        if num < 10:
            return False
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        num_str = str(num)
        for i in range(1, len(num_str)):
            if int(num_str[i:]) % 2 == 0 or int(num_str[i:]) % 3 == 0 or int(num_str[i:]) % 5 == 0 or (int(num_str[i:]) % 7 == 0):
                return False
            if int(num_str[:-i]) % 2 == 0 or int(num_str[:-i]) % 3 == 0 or int(num_str[:-i]) % 5 == 0 or (int(num_str[:-i]) % 7 == 0):
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes