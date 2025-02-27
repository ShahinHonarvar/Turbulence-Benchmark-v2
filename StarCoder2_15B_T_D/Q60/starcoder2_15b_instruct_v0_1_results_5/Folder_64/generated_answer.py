def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[4]
    truncatable_primes = []
    for number in range(2, x + 1):
        is_truncatable_prime = True
        for i in range(len(str(number)) - 1):
            truncated_number_left = int(str(number)[i:])
            truncated_number_right = int(str(number)[:len(str(number)) - i])
            if not is_prime(truncated_number_left) or not is_prime(truncated_number_right):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(number)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True