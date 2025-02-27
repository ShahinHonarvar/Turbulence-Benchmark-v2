def all_right_truncatable_prime(input_tuple):
    x = input_tuple[177]
    right_truncatable_primes = []
    for number in range(2, x):
        is_right_truncatable = True
        for digit in str(number):
            if int(digit) % 2 == 0:
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True