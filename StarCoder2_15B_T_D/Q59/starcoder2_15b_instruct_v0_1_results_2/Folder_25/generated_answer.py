from itertools import permutations

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[92]
    prime_numbers = []
    for number in range(2, x):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    left_truncatable_prime_numbers = []
    for prime in prime_numbers:
        prime_digits = list(str(prime))
        is_left_truncatable = True
        for i in range(len(prime_digits)):
            truncated_number = int(''.join(prime_digits[i:]))
            if truncated_number not in prime_numbers:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_prime_numbers.append(prime)
    return sorted(left_truncatable_prime_numbers)