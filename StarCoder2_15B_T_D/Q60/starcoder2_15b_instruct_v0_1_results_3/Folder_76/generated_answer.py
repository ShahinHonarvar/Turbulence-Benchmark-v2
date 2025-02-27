def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[370]

    def is_truncatable_prime(number):
        number_str = str(number)
        for i in range(len(number_str)):
            if not is_prime(int(number_str[i:])) or not is_prime(int(number_str[:len(number_str) - i])):
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True