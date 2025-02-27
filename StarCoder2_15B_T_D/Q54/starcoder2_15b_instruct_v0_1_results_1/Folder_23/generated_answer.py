def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for number in numbers:
        if number < 10:
            continue
        while number > 10:
            if not is_prime(number):
                break
            number //= 10
        if is_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True