def all_right_truncatable_prime(input_tuple):
    x = input_tuple[42]
    right_truncatable_primes = []
    for number in range(2, x):
        is_right_truncatable_prime = True
        for digit in str(number)[::-1]:
            if not is_prime(int(digit)):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(number)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True