def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]
    left_truncatable_primes = []
    for i in range(1, x):
        if is_prime(i):
            digits = [int(digit) for digit in str(i)]
            is_left_truncatable = True
            for j in range(len(digits) - 1):
                truncated_number = int(''.join((str(digit) for digit in digits[j + 1:])))
                if not is_prime(truncated_number):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True