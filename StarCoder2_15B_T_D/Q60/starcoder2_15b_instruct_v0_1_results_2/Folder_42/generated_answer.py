def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[64]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        is_left_right_truncatable_prime = True
        current_number = i
        while len(str(current_number)) > 1:
            if not is_prime(current_number):
                is_left_right_truncatable_prime = False
                break
            current_number = int(str(current_number)[1:])
            if not is_prime(current_number):
                is_left_right_truncatable_prime = False
                break
            current_number = int(str(current_number)[:-1])
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True