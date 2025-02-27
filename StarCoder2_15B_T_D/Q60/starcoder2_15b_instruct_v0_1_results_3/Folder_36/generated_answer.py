def all_left_right_truncatable_prime(numbers):
    left_truncatable_primes = []
    right_truncatable_primes = []
    x = numbers[992]
    for i in range(2, x + 1):
        is_left_truncatable = True
        is_right_truncatable = True
        current_number = i
        while current_number >= 10:
            if current_number % 10 == 0:
                is_left_truncatable = False
                break
            if not is_prime(current_number):
                is_left_truncatable = False
                break
            current_number //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
        current_number = i
        while current_number >= 10:
            if current_number % 10 == 0:
                is_right_truncatable = False
                break
            if not is_prime(current_number):
                is_right_truncatable = False
                break
            current_number %= 10 ** (len(str(current_number)) - 1)
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    left_right_truncatable_primes = [prime for prime in left_truncatable_primes if prime in right_truncatable_primes]
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True