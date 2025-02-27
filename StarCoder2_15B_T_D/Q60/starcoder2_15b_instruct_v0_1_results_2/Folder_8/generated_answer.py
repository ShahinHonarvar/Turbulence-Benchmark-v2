def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for number in numbers:
        if number < 10:
            continue
        is_truncatable = True
        for i in range(1, len(str(number))):
            left_truncation = int(str(number)[i:])
            right_truncation = int(str(number)[:len(str(number)) - i])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True