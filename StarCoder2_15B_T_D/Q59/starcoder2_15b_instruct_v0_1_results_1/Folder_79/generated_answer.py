def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[91]
    left_truncatable_primes = []
    for number in tuple_of_positive_integers:
        if number < 10 and is_prime(number):
            left_truncatable_primes.append(number)
        elif number >= 10:
            digits = [int(digit) for digit in str(number)]
            for i in range(len(digits) - 1):
                truncated_number = int(''.join((str(digit) for digit in digits[i + 1:])))
                if not is_prime(truncated_number):
                    break
            else:
                left_truncatable_primes.append(number)
    left_truncatable_primes.sort()
    return left_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True